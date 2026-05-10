# 🤖 Chatbot d'Entreprise (chatbot)

Cet agent est un assistant virtuel nommé **Assiste**, conçu pour fournir des informations précises et amicales sur l'entreprise fictive **Acme Corp**.

## 🚀 Fonctionnalités
- **Assistant Virtuel** : Répond aux questions des utilisateurs de manière polie et informative.
- **Base de Connaissances** : Utilise des données spécifiques à l'entreprise (FAQ, produits, horaires) pour répondre.
- **Interface Gradio** : Une interface web conviviale pour interagir avec le chatbot.
- **API REST (FastAPI)** : Un point de terminaison API pour intégrer le chatbot dans d'autres systèmes.

## 🛠️ Technologies
- **Frameworks** : FastAPI, Gradio
- **Modèle LLM** : `gpt-oss:120b-cloud` (via Ollama)
- **Langage** : Python

## 📁 Structure du projet
- `main.py` : Lance l'interface utilisateur web avec Gradio.
- `app.py` : Serveur FastAPI pour l'accès via API.
- `__pycache__` : Fichiers de cache Python.

## ⚙️ Installation & Utilisation

### 1. Installation
Installez les dépendances nécessaires (si ce n'est pas déjà fait au niveau global) :
```bash
pip install fastapi uvicorn requests gradio
```

### 2. Lancement de l'Interface Web
Pour interagir avec le chatbot via votre navigateur :
```bash
python main.py
```

### 3. Lancement de l'API
Pour démarrer le serveur API :
```bash
uvicorn app:app --reload
```

## 📝 Exemple de Contexte Utilisé
Le chatbot est initialisé avec un contexte incluant le nom de l'entreprise, sa description et une FAQ simplifiée pour garantir des réponses pertinentes sur les produits phares, le support technique et les horaires.
