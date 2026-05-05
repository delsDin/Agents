# 🔍 Extracteur NER (Named Entity Recognition)

Ce projet est un agent d'intelligence artificielle spécialisé dans la reconnaissance d'entités nommées. Il analyse un texte brut pour en extraire des informations structurées telles que des noms de personnes, des organisations, des lieux, des dates, des monnaies et des quantités.

## 🚀 Fonctionnalités

-   **Extraction Multi-Entités** : Identifie les personnes, organisations, localisations, dates, quantités et monnaies.
-   **Format de Sortie Clair** : Présente les résultats sous forme de liste à puces facile à lire.
-   **Double Interface** : 
    -   API REST via FastAPI.
    -   Interface Web interactive via Gradio.
-   **Support Cloud** : Option pour utiliser des modèles plus puissants via Ollama Cloud.

## 🛠️ Installation

1.  Assurez-vous d'avoir **Ollama** installé avec le modèle `llama3.2:1b`.
2.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
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
```bash
OLLAMA_API_KEY="votre_cle" uvicorn app_cloud:app --reload
```

## 🌟 Cas d'usage

-   **Analyse de Documents** : Extraire rapidement les points clés (qui, où, quand) de rapports ou d'articles.
-   **Veille Informationnelle** : Identifier les entreprises ou les personnalités mentionnées dans des flux de nouvelles.
-   **Structuration de Données** : Transformer des textes non structurés en listes d'entités exploitables.
-   **Assistance Juridique/Administrative** : Repérer les dates importantes et les entités légales dans des contrats.

## 📂 Structure du projet
-   `app.py` : Serveur FastAPI local.
-   `app_cloud.py` : Serveur FastAPI Cloud.
-   `main.py` : Interface utilisateur Gradio.
-   `requirements.txt` : Dépendances du projet.
