from pathlib import Path

def read_file(path: str) -> str:
    """
    Lit le contenu d'un fichier article (Markdown ou texte)
    et retourne le texte brut.
    """
    return Path(path).read_text(encoding="utf-8")