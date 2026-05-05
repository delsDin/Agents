from fastapi import FastAPI
import requests

# Initialisation de l'application FastAPI
app = FastAPI()

# URL de l'API locale d'Ollama pour la génération de texte
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate/")
def generate_text(prompt: str, word_limit: int = 100):
    """
    Point de terminaison API pour générer du texte.
    Prend un prompt et une limite de mots en entrée.
    """
    
    # Construction du prompt complet avec la contrainte de longueur
    full_prompt = f"Génère une reponse avec {word_limit} mots :\n\n{prompt}"

    # Configuration de la requête pour Ollama
    payload ={
        "model": "llama3.2:1b",
        "prompt": full_prompt,
        "stream": False # On désactive le streaming pour recevoir la réponse complète d'un coup
    }

    # Envoi de la requête POST à Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    # Retourne le texte généré ou un message par défaut en cas d'échec
    return response.json().get("response", "Contenu non généré.")

# Pour lancer le serveur, utilisez la commande : uvicorn app:app --reload