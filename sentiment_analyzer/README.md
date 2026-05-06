# 🎭 Analyseur de Sentiment (sentiment_analyzer)

Cet agent est un expert en analyse de sentiment. Il évalue la tonalité d'un texte et lui attribue un score sur 10 (score de satisfaction ou de joie).

## 🚀 Fonctionnalités
- **Analyse de Sentiment** : Évaluation précise du ton du texte.
- **Score /10** : Attribution d'une note numérique pour quantifier le sentiment.
- **Interface Gradio** : Une interface web simple pour tester l'analyseur localement.
- **API REST (FastAPI)** : Endpoints pour intégrer l'analyseur dans d'autres applications (support Local et Cloud).

## 🛠️ Technologies
- **Frameworks** : FastAPI, Gradio
- **Modèles LLM** : 
  - Local : `llama3.2:1b` (via Ollama)
  - Cloud : `gpt-oss:120b` (via Ollama Cloud)

## 📁 Structure du projet
- `main.py` : Lance l'interface utilisateur web avec Gradio.
- `app.py` : Serveur FastAPI pour l'utilisation locale d'Ollama.
- `app_cloud.py` : Serveur FastAPI configuré pour utiliser Ollama Cloud.
- `requirements.txt` : Liste des dépendances Python nécessaires.

## ⚙️ Installation & Utilisation

### 1. Installation
Assurez-vous d'avoir installé les dépendances :
```bash
pip install -r requirements.txt
```

### 2. Lancement (Local)
Pour lancer l'interface web :
```bash
python main.py
```

Pour lancer l'API locale :
```bash
uvicorn app:app --reload
```

### 3. Lancement (Cloud)
Pour utiliser l'API avec Ollama Cloud :
```bash
OLLAMA_API_KEY="votre_cle_api" uvicorn app_cloud:app --reload
```

## 📝 Exemple de Prompt utilisé
> "Tu es un expert en analyse de sentiment. Analyse le texte ci-dessous et fournis un score de sentiment sur 10 (0 = très négatif, 5 = neutre, 10 = très positif).
>
> Format de réponse attendu :
> Score : [Note]/10
> Sentiment : [Positif/Neutre/Négatif]
> Explication : [Courte justification]
>
> Texte : [TEXTE]"
