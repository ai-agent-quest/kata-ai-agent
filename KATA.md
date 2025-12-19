## 🎯 Contexte Général
Vous êtes chercheur·se et vous devez analyser des dizaines d'articles scientifiques pour votre revue de hebdomadaire.<br>
Votre mission est de construire un agent AI qui automatise l'analyse, la synthèse et l'enrichissement de la littérature académique.


1. Intéraction avec un appel
2. Interact with dspy Prediction
3. Information Extraction
4. Chain of Thought
4. Refine (Classification)
6. ReAct (MCP Tools)


1- Présentation kata
2- Communicate with LLM using an HTTP request
3- Communicate with LLM using DSPy (Avec Cache(par défaut), puis sans cache)

---
🧠 Kata — Assistant de Recherche Académique

    Progression par capacités d’agent

    🟢 Introduction — LLM brut → Agent structuré

        But : Comprendre pourquoi un simple appel LLM ne suffit pas

        Appel HTTP direct à un LLM

        Résumé “à la main” via prompt

        Constats : sorties instables, peu exploitables, difficilement automatisables

        Introduction d’une couche de structure (inputs / outputs explicites)

        👉 Message clé : un agent ≠ un prompt

    🔹 Module 1 — Résumé Exécutif

        Capacité ajoutée : Compression sémantique

        Input : abstract ou texte scientifique

        Output : résumé ultra-concis (2–3 phrases)

        Objectif métier : décider rapidement
        Lire / Ignorer / Mettre de côté

        👉 L’agent apprend à réduire l’information pour agir

    🔹 Module 2 — Extraction d’Information

        Capacité ajoutée : Structuration du savoir

        Transformation du texte libre en données exploitables

        Extraction : métadonnées, contributions, méthodes, résultats, limites

        Sortie structurée et cohérente

        👉 L’agent apprend à construire un modèle du monde

    🔹 Module 3 — Analyse Critique (Raisonnement)

        Capacité ajoutée : Évaluation raisonnée et explicable

        Analyse selon plusieurs critères :

        originalité

        rigueur

        validation

        impact

        reproductibilité

        Justification explicite pour chaque point

        Score global argumenté

        👉 L’agent apprend à juger, pas seulement décrire

    🔹 Module 4 — Classification Raffinée

        Capacité ajoutée : Décision hiérarchique et contextuelle

        Classification progressive :

        domaine → sous-domaine → technique → positionnement

        Mise en contexte par rapport à ta recherche

        Estimation de la pertinence

        👉 L’agent apprend à situer une information dans un espace de décision

    🔹 Module 5 — Agent Autonome (ReAct)

        Capacité ajoutée : Interaction avec l’environnement

        L’agent choisit quand et comment utiliser des outils externes :

        recherche d’articles

        citations

        code

        benchmarks

        prestige des conférences

        Raisonnement + action + observation

        Synthèse enrichie et recommandation finale

        👉 L’agent apprend à explorer, comparer et recommander seul

    🏁 Résultat Final

        Un assistant de recherche académique capable de :

        comprendre un article

        l’analyser de manière critique

        le positionner dans la littérature

        enrichir l’analyse avec des sources externes

        produire une recommandation exploitable