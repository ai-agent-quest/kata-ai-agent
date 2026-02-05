# Kata AI Agent

Ce projet contient de nombreux exercices utiles pour le développement d'agent IA basé sur `Python`.

## Contexte et Objectif du Kata

Ce kata vous permet de progresser étape par étape dans le développement d'un agent intelligent capable de :
- Comprendre et résumer des documents
- Extraire des informations structurées
- Effectuer une analyse critique
- Interagir avec des outils externes pour enrichir ses connaissances
- Gérer des workflows complexes

## Structure du Kata

### 1. Interaction avec un LLM (Language Model)
Les bases de l'interaction avec les modèles linguistiques.
#### Exercices :
1. [Appel à un llm via une simple requête http](notebook/01-interact-with-llm/01-simple-call-http.ipynb)
   *Objectif : Comprendre comment faire directement appel à un LLM via HTTP*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/01-simple-call-http/notebook/01-interact-with-llm/01-simple-call-http.ipynb)

2. [Utilisation du framework dsPy](notebook/01-interact-with-llm/02-prediction.ipynb)
   *Objectif : Utiliser le framework dsPy pour structurer les interactions avec les LLM*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/02-prediction/notebook/01-interact-with-llm/02-prediction.ipynb)

3. [Chaines de pensée](notebook/01-interact-with-llm/03-chain-of-thought.ipynb)
   *Objectif : Implémenter des raisonnements complexes en utilisant la méthode Chain of Thought*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/03-chain-of-thought/notebook/01-interact-with-llm/03-chain-of-thought.ipynb)

4. [Structurer les sorties des LLM](notebook/01-interact-with-llm/04-structured-output.ipynb)
   *Objectif : Obtenir des sorties structurées et prévisibles à partir des LLM*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/04-structured-output/notebook/01-interact-with-llm/04-structured-output.ipynb)

### 2. LLM Augmenté
Amélioration de l'interaction avec les LLM en leur fournissant des contextes ou des outils.
![Augmented LLM](assets/augmented-llm.png)

#### Exercices :
5. [Utilisation d'outils](notebook/02-augmented-llm/05-tool-call.ipynb)
   *Objectif : Intégrer des outils externes dans les interactions avec les LLM*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/05-tool-call/notebook/02-augmented-llm/05-tool-call.ipynb)

6. [RAG (Retrieval Augmented Generation)](notebook/02-augmented-llm/06-rag.ipynb)
   *Objectif : Utiliser des documents externes pour enrichir les réponses des LLM*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/06-rag/notebook/02-augmented-llm/06-rag.ipynb)

7. [Utilisation de la mémoire](notebook/02-augmented-llm/07-memory.ipynb)
   *Objectif : Maintenir un contexte de conversation persistant*
   
      [Solution](https://github.com/ai-agent-quest/kata-ai-agent/blob/07-memory/notebook/02-augmented-llm/07-memory.ipynb)

### 3. Agent Autonome
Développement d'agents capables d'agir indépendamment.
![alt text](assets/autonomous-agent)

#### Exercices :
8. [Agent autonome](notebook/03-autonomous-agent/08-autonomous-agent.py)
   *Objectif : Créer un agent capable de planifier et exécuter des actions autonomes*

### 4. Workflow Agentique
Gestion de workflows complexes avec plusieurs agents.
![alt text](assets/routing-llm.png)

#### Exercices :
9. [Workflow](notebook/04-workflow/09-workflow.ipynb)  
   *Objectif : Orchestration d'agents dans un workflow complexe*

10. [Observabilité et évaluation](notebook/04-workflow/10-evaluation.ipynb)  
    *Objectif : Évaluer et observer les performances des agents*

## Technologies Utilisées

Ce projet utilise plusieurs bibliothèques et outils :
- **dsPy** : Pour structurer les interactions avec les LLM
- **Docling** : Pour le traitement de documents PDF
- **Qdrant** : Pour la gestion de vecteurs et RAG
- **Jupyter Notebook** : Pour l'expérimentation interactive
- **LangChain** : Pour l'intégration d'outils et de chaînes

## Comment Exécuter les Exercices

### Installation des dépendances
```bash
pip install -e .
```

### Exécution d'un notebook spécifique
```bash
jupyter nbconvert --execute notebook/01-interact-with-llm/01-simple-call-http.ipynb
```

### Exécution d'un script Python
```bash
python notebook/03-autonomous-agent/08-autonomous-agent.py
```