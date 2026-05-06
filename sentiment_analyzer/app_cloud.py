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
        f"Tu es un expert en analyse de sentiment. Donne un score /10 du texte suivant :\n\n{text}"
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