from fastapi import FastAPI
import requests

# Initialisation de l'application FastAPI pour le correcteur grammatical
app = FastAPI()

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/correct/")
def correct_grammar(text : str):
    """
    Point de terminaison API pour corriger le texte.
    Envoie le texte à Llama 3.2 pour correction et explications.
    """

    # Instruction spécifique pour le modèle : correction + explications
    prompt = f"Corrige toutes les erreurs de grammaire et d'orthographe dans le texte suivant et fournis des explications:\n\n{text}"
    
    # Configuration du payload pour Ollama
    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False # Réception de la réponse complète
    }

    # Appel à l'API locale d'Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    # Retourne la réponse corrigée ou un message d'erreur
    return response.json().get("response", "Aucune correction générée")

# Pour lancer le serveur, utiliser la commande : uvicorn app:app --reload