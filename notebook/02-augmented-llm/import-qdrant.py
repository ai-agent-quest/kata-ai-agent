import logging
from qdrant_client import QdrantClient, models
from docling.document_converter import DocumentConverter
from dotenv import dotenv_values
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer
from docling_core.transforms.chunker.hybrid_chunker import DocChunk, HybridChunker
from docling_core.types.doc import DoclingDocument
from docling.datamodel.base_models import InputFormat


config = dotenv_values(".env")
source = "assets/books/livre-recette.pdf"
source_md = "assets/books/livre-recette.md"
qdrant_url = config.get('QDRANT_URL')
qdrant_api_key = config.get('QDRANT_API_KEY')
collection_name = "livre-recette"
embed_model_id = "manu/bge-fr-en"
embedder = SentenceTransformer(embed_model_id)


def parse_document(doc_source: str, inputFormat: InputFormat.PDF):
    logging.info(f"Reading pdf document: {doc_source}")
    doc_converter = DocumentConverter(allowed_formats=[inputFormat])
    result = doc_converter.convert(doc_source)
    logging.info(f"pdf document: {doc_source} read")
    logging.debug(result.document.export_to_markdown())
    return result


def write_document_markdown(doc_path: str, content: str):
    logging.info(f"Writting markdown document: {doc_path}")
    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(content)
    logging.info(f"Markdown document writted")


def fix_markdown_document(doc_path: str):
    logging.info(f"Fixing document : {doc_path}")
    with open(doc_path, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    nouvelles_lignes = []
    for ligne in lignes:
        if ligne.strip() == "## LIVRE DE RECETTES ETUDIANTS PAUVRES POUR":
            nouvelles_lignes.append("# LIVRE DE RECETTES POUR ETUDIANTS PAUVRES\n")
        elif ligne.strip() == "## (A PARTAGER)":
            # Doing nothing
            nouvelles_lignes.append("\n")
        elif ligne.strip() == "## NACHOS GARNIS entrees":
            nouvelles_lignes.append("## NACHOS GARNIS entrees (A PARTAGER)\n")
        elif ligne.strip() == "## INGREDIENTS":
            nouvelles_lignes.append("### INGREDIENTS\n")
        elif ligne.strip() == "## PREPARATION":
            nouvelles_lignes.append("### PREPARATION\n")
        else:
            nouvelles_lignes.append(ligne)

    with open(doc_path, "w", encoding="utf-8") as f:
        f.writelines(nouvelles_lignes)

    logging.info("Document fixed")


def create_collection(collection_name: str, client: QdrantClient):
    logging.info(f"Recreate Qdrant collection : {collection_name}")
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config={
            "recette": models.VectorParams(
                size=1024,
                distance=models.Distance.COSINE,
            )
        }
    )
    logging.info("Qdrant collection created")
        
        
def embed(text: str):
    return embedder.encode(text).tolist()


def embedding_text(chunk: DocChunk):
    if chunk.meta.headings and len(chunk.meta.headings) > 2 :
        return chunk.meta.headings[1]
    return chunk.text


def raw_text(chunk: DocChunk):
    if chunk.meta.headings:
        return "title=" + " > ".join(chunk.meta.headings) + " | text=" + chunk.text
    return chunk.text


def build_payload(index: int, chunk: DocChunk):
    return {
        "doc_id": chunk.meta.origin.filename if chunk.meta.origin and chunk.meta.origin.filename else None,

        # hiérarchie
        "section_path": chunk.meta.headings,
        "section_level": len(chunk.meta.headings) if chunk.meta.headings else None,
        "section_title": chunk.meta.headings[-1] if chunk.meta.headings else None,

        # contenu
        "content": chunk.text,
        "text": raw_text(chunk),

        # navigation
        "chunk_index": index,
        "page_numbers":  list(dict.fromkeys([
            prov.page_no
            for item in chunk.meta.doc_items
            for prov in item.prov
            if hasattr(prov, "page_no")
        ]))
    }


def chunk_document(inputDocument: DoclingDocument):    
    logging.info("Chunking document")
    chunker = HybridChunker(
        merge_peers=True,
        always_emit_headings=True
    )
    chunks = list(chunker.chunk(inputDocument))

    points = []

    for i, chunk in enumerate(chunks):
        points.append(
            PointStruct(
                id=i,
                vector={
                    "recette": embed(embedding_text(chunk))
                },
                payload=build_payload(i, chunk),
            )
        )
    logging.info("Document chunked")
    return points


def upload_chunk_into_qdrant_collection(collection_name: str, client: QdrantClient, points: list[PointStruct]):
    batch_size = 64
    for i in range(0, len(points), batch_size):
        client.upsert(
            collection_name=collection_name,
            points=points[i:i+batch_size]
        )


def upload_recette_into_qdrant(collection_name: str, should_create_collection: bool):
    logging.info('Upload started')
    client = QdrantClient(qdrant_url, api_key=qdrant_api_key)
    if should_create_collection :
        create_collection(collection_name, client)

    source_doc = parse_document(source, InputFormat.PDF)
    write_document_markdown(source_md, source_doc.document.export_to_markdown())
    fix_markdown_document(source_md)
    sanitized_doc = parse_document(source_md, InputFormat.MD)
    points = chunk_document(sanitized_doc.document)
    
    upload_chunk_into_qdrant_collection(collection_name, client, points)
    logging.info('Upload completed')


logging.basicConfig(level=logging.INFO) 
upload_recette_into_qdrant(collection_name, True)
