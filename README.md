# 🤖 UDEMY AI Agents Collection

Ce dépôt regroupe plusieurs projets d'agents d'intelligence artificielle développés dans le cadre d'une formation Udemy. Chaque projet explore une facette différente de l'utilisation des modèles de langage (LLM) locaux avec **Ollama**.

## 📂 Contenu du dépôt

### 1. [Générateur de Texte (text_generateur)](./text_generateur/README.md)
Un agent capable de générer du contenu textuel à partir d'un prompt utilisateur, avec une limite de mots ajustable.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:1b).
-   **Fonctionnalités** : API REST et Interface Web.

### 2. [Résumeur de Texte (text_summarize)](./text_summarize/README.md)
Un agent spécialisé dans la synthèse de documents. Il peut prendre un ou deux textes en entrée et produire un résumé fidèle.
-   **Technologies** : FastAPI, Gradio, Ollama (Llama 3.2:1b).
-   **Fonctionnalités** : Extraction de l'essentiel, support multi-documents.

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
