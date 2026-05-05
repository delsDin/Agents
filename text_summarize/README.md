# 🤖 AI Text Summarizer (Résumeur de Texte IA)

Ce projet propose deux interfaces (une API et une interface graphique) pour résumer du texte en utilisant le modèle **Llama 3.2:1b** via **Ollama**. Vous pouvez remplacer ce modèle par n'importe quel modèle compatible avec Ollama.

## 🚀 Fonctionnalités

*   **API FastAPI** (`app.py`) : Une interface programmatique pour envoyer des textes et recevoir des résumés.
*   **Interface Gradio** (`text_summarize.py`) : Une interface web conviviale pour coller du texte et voir le résumé instantanément.
*   **Support multi-textes** : Possibilité de combiner deux textes pour un résumé global.

## 🛠 Prérequis

1.  **Ollama** doit être installé sur votre machine. [Télécharger Ollama](https://ollama.com/).
2.  Le modèle **Llama 3.2:1b** doit être téléchargé :
    ```bash
    ollama pull llama3.2:1b
    ```
3.  **Python 3.8+** installé.

## 📦 Installation

Installez les dépendances nécessaires en utilisant le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

## 📋 Utilisation

### 1. Interface Web (Gradio)
C'est la méthode la plus simple pour tester visuellement.
```bash
python text_summarize.py
```
Ensuite, ouvrez l'URL locale (généralement `http://127.0.0.1:7860`) dans votre navigateur.

### 2. API (FastAPI)
Idéal pour intégrer ce service dans d'autres applications.
```bash
uvicorn app:app --reload
```
L'API sera accessible sur `http://127.0.0.1:8000/summarize/`.

## 📂 Structure du projet

*   `app.py` : Serveur API utilisant FastAPI.
*   `text_summarize.py` : Interface utilisateur web utilisant Gradio.
*   `.gitignore` : Fichiers à ignorer par Git.
*   `README.md` : Documentation du projet.

---
*Développé pour simplifier le résumé de documents longs grâce à l'IA locale.*
