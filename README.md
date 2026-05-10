# 🤖 AI Agents Collection

Ce dépôt regroupe plusieurs projets d'agents d'intelligence artificielle développés dans le cadre d'une formation Udemy. Chaque projet explore une facette différente de l'utilisation des modèles de langage (LLM) locaux avec **Ollama**.

## 📂 Contenu du dépôt

### 1. [Générateur de Texte (text_generator)](./text_generator/README.md)
Un agent capable de générer du contenu textuel à partir d'un prompt utilisateur, avec une limite de mots ajustable.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:1b), Ollama Cloud.
-   **Fonctionnalités** : API REST (Locale & Cloud) et Interface Web.

### 2. [Résumeur de Texte (text_summarize)](./text_summarize/README.md)
Un agent spécialisé dans la synthèse de documents. Il peut prendre un ou deux textes en entrée et produire un résumé fidèle.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:1b).
-   **Fonctionnalités** : Extraction de l'essentiel, support multi-documents.

### 3. [Correcteur Grammatical (grammar_checker)](./grammar_checker/README.md)
Un agent qui corrige l'orthographe et la grammaire tout en fournissant des explications pédagogiques.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:3b), Ollama Cloud.
-   **Fonctionnalités** : Correction textuelle, explications détaillées, support Cloud.

### 4. [Extracteur NER (ner)](./ner/README.md)
Un agent capable d'extraire les entités nommées (personnes, lieux, organisations) d'un texte.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:1b), Ollama Cloud.
-   **Fonctionnalités** : Identification d'entités, structuration de données, support Cloud.

### 5. [Analyseur de Sentiment (sentiment_analyzer)](./sentiment_analyzer/README.md)
Un agent spécialisé dans l'analyse de sentiment, attribuant un score de satisfaction sur 10.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:1b), Ollama Cloud.
-   **Fonctionnalités** : Évaluation de tonalité, notation numérique, support Cloud.

### 6. [Chatbot d'Entreprise (chatbot)](./chatbot/README.md)
Un assistant virtuel nommé "Assiste" capable de répondre aux questions sur une entreprise (Acme Corp).
-   **Technologies** : FastAPI, Gradio, Ollama (gpt-oss:120b-cloud).
-   **Fonctionnalités** : Support client automatisé, FAQ interactive, interface amicale.

## 🛠️ Configuration Globale



### Prérequis
-   **Python 3.8+**
-   **Ollama** installé et configuré avec le modèle `llama3.2:1b`.

### Installation des dépendances
Il est recommandé d'utiliser un environnement virtuel :
```bash
python -m venv .venv_agent
source .venv_agent/bin/activate  # Sur Linux
pip install -r requirements.txt
```

## 🚀 Lancement des Agents

Chaque dossier contient ses propres scripts de lancement. Reportez-vous aux README spécifiques pour plus de détails.
-   **API** : `uvicorn app:app --reload` (dans le dossier de l'agent)
-   **Web UI** : `python main.py` ou `python <nom_du_script>.py`

---
---
---

*Notice : Commentaires auto par IA*
---
---
---