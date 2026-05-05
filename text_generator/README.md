# 🤖 Text Générateur

Ce projet est une application de génération de texte basée sur l'intelligence artificielle. Elle utilise le modèle **Llama 3.2 (1b)** via l'outil **Ollama** pour produire du contenu textuel à partir de prompts fournis par l'utilisateur.

Le projet propose deux manières d'interagir avec le modèle :
1.  **API REST** avec FastAPI.
2.  **Interface Graphique (Web)** avec Gradio.

## 🚀 Prérequis

Avant de commencer, assurez-vous d'avoir installé :
-   [Python 3.8+](https://www.python.org/)
-   [Ollama](https://ollama.com/) avec le modèle `llama3.2:1b` installé (`ollama run llama3.2:1b`).

## 🛠️ Installation

1.  Clonez ou copiez les fichiers du projet.
2.  Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Utilisation

### 1. Version API (FastAPI)
Pour lancer le serveur API :
```bash
uvicorn app:app --reload
```
L'API sera accessible sur `http://127.0.0.1:8000`. Vous pouvez tester le point de terminaison `/generate/` via la documentation interactive à `http://127.0.0.1:8000/docs`.

### 2. Version Interface Web (Gradio)
Pour lancer l'interface graphique :
```bash
python main.py
```
Une URL locale (généralement `http://127.0.0.1:7860`) s'affichera dans le terminal. Ouvrez-la dans votre navigateur pour utiliser le générateur.

## 🌟 Cas d'usage

Ce générateur de texte peut être utilisé dans de nombreux scénarios :

-   **Rédaction de contenu** : Création de brouillons pour des articles de blog, des emails ou des publications sur les réseaux sociaux.
-   **Brainstorming** : Génération d'idées de titres, de thèmes ou de plans pour des projets créatifs.
-   **Assistance à l'écriture** : Aide pour surmonter le syndrome de la page blanche en générant des paragraphes de départ.
-   **Traduction et Reformulation** : Demander à l'IA de reformuler un texte pour changer de ton ou de style.
-   **Éducation** : Génération d'explications simples sur des concepts complexes.
-   **Développement de Chatbots** : Utilisation de l'API comme moteur de réponse pour un bot conversationnel.

## 📂 Structure du projet

-   `app.py` : Serveur FastAPI exposant l'API de génération.
-   `main.py` : Interface utilisateur web construite avec Gradio.
-   `requirements.txt` : Liste des bibliothèques Python requises.
