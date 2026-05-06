from fastapi import FastAPI
import requests

# Initialisation de l'application FastAPI pour l'extracteur d'entités nommées (NER)
app = FastAPI()

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/sentiment/")
def generate_text(text: str):
    """
    """
    
    prompt = (
        f"Tu es un expert en analyse de sentiment. Donne un score /10 du texte suivant :\n\n{text}"
    )

    # Configuration de la requête pour Ollama
    payload ={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }

    # Envoi de la requête POST à Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    # Retourne le texte extrait ou un message d'erreur par défaut
    return response.json().get("response", "Texte non noté.")

# Pour lancer le serveur, utilisez la commande : uvicorn app:app --reload