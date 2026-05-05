# ✍️ Correcteur Grammatical IA

Ce projet est un agent d'intelligence artificielle capable de détecter et de corriger les erreurs d'orthographe et de grammaire. Contrairement à un correcteur classique, il fournit également des explications détaillées sur les corrections apportées pour aider l'utilisateur à s'améliorer.

## 🚀 Fonctionnalités

-   **Correction Avancée** : Utilise Llama 3.2 pour une compréhension contextuelle fine.
-   **Explications Pédagogiques** : Chaque correction est accompagnée d'une explication.
-   **Double Interface** : 
    -   Une API REST performante.
    -   Une interface web intuitive.
-   **Support Cloud** : Option pour utiliser l'API cloud d'Ollama pour des modèles plus puissants.

## 🛠️ Installation

1.  Assurez-vous d'avoir **Ollama** avec le modèle `llama3.2:3b`.
2.  Installez les dépendances :
    ```bash
    pip install fastapi requests gradio ollama
    ```

## 💻 Utilisation

### Version Locale (API)
```bash
uvicorn app:app --reload
```

### Version Locale (Web UI)
```bash
python main.py
```

### Version Cloud (API)
Nécessite une clé API Ollama Cloud.
```bash
OLLAMA_API_KEY="votre_cle" uvicorn app_cloud:app --reload
```

## 🌟 Cas d'usage

-   **Rédaction Professionnelle** : Vérifier des emails ou des rapports avant envoi.
-   **Apprentissage des Langues** : Comprendre ses erreurs récurrentes grâce aux explications de l'IA.
-   **Édition de Contenu** : Améliorer la qualité de textes longs ou d'articles de blog.
-   **Assistance au Code** : Bien que focalisé sur le texte, il peut aider à rédiger des documentations sans fautes.

## 📂 Fichiers
-   `app.py` : Version API locale.
-   `app_cloud.py` : Version API utilisant le cloud.
-   `main.py` : Interface graphique Gradio.
