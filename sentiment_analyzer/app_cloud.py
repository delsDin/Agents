import os
from fastapi import FastAPI
from ollama import Client


app = FastAPI()


client = Client(
    host='https://ollama.com',
    headers={'Authorization': f"Bearer {os.environ.get('OLLAMA_API_KEY')}"}
)

@app.post("/sentiment/")
def generate_text(text: str):
    """
    """
    
    
    prompt = (
        f"Tu es un expert en analyse de sentiment. Analyse le texte ci-dessous et fournis un score de sentiment sur 10 (0 = très négatif, 5 = neutre, 10 = très positif).\n\n"
        f"Format de réponse attendu :\n"
        f"Score : [Note]/10\n"
        f"Sentiment : [Positif/Neutre/Négatif]\n"
        f"Explication : [Courte justification]\n\n"
        f"Texte : {text}"
     )

    try:
        # Appel au modèle Cloud (ex: gpt-oss:120b) via le client Python officiel
        response = client.chat(
            model='gpt-oss:120b',
            messages=[{'role': 'user', 'content': prompt}],
            stream=False # Réception directe de la réponse
        )
        
        # Retourne le contenu extrait par le modèle
        return {"response": response.message.content}

    except Exception as e:
        # Gestion des erreurs d'authentification ou de réseau
        return {"error": f"Erreur avec Ollama Cloud : {str(e)}"}

# Lancement : OLLAMA_API_KEY="votre_cle" uvicorn app_cloud:app --reload