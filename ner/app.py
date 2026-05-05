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
    
    # Construction du prompt demandant une extraction sous forme de liste à puces
    full_prompt = f"Extrait toutes les entités nommées (personnes, organisations, lieu, monnaie, quantité, dates) s'ils y en a avec une liste à puces du texte suivant :\n\n{text}"

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