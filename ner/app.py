from fastapi import FastAPI
import requests

# Initialisation de l'application FastAPI pour l'extracteur d'entités nommées (NER)
app = FastAPI()

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/ner/")
def generate_text(text: str):
    """
    Point de terminaison API pour extraire les entités nommées d'un texte.
    Identifie les personnes, lieux, organisations, dates, etc.
    """
    
    # Prompt optimisé pour une extraction structurée et précise
    full_prompt = (
        "Tu es un expert en extraction d'entités nommées. Analyse le texte ci-dessous et extrait "
        "UNIQUEMENT les entités suivantes : PERSONNE, ORGANISATION, LIEU, DATE, MONNAIE, QUANTITÉ.\n\n"
        "Règles :\n"
        "1. Présente le résultat sous forme de liste à puces classée par catégorie.\n"
        "2. Ne fais aucun commentaire supplémentaire.\n"
        "3. Si aucune entité n'est trouvée, réponds : 'Aucune entité détectée.'\n\n"
        f"Texte à analyser :\n{text}"
    )

    # Configuration de la requête pour Ollama
    payload ={
        "model": "llama3.2:1b",
        "prompt": full_prompt,
        "stream": False # Réception de la réponse complète sans streaming
    }

    # Envoi de la requête POST à Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    # Retourne le texte extrait ou un message d'erreur par défaut
    return response.json().get("response", "Contenu non généré.")

# Pour lancer le serveur, utilisez la commande : uvicorn app:app --reload