import os
from fastapi import FastAPI
from ollama import Client

# Initialisation de l'application FastAPI
app = FastAPI()

# Configuration du client Ollama pour une utilisation via une instance distante ou Cloud
# La clé API est récupérée de manière sécurisée via une variable d'environnement
client = Client(
    host='https://ollama.com',
    headers={'Authorization': f"Bearer {os.environ.get('OLLAMA_API_KEY')}"}
)

@app.post("/generate/")
def generate_text(prompt: str, word_limit: int = 100):
    """
    Point de terminaison pour la génération via le SDK Ollama Cloud.
    Utilise des modèles plus massifs pour une meilleure qualité de réponse.
    """
    
    # Construction du prompt avec contrainte de longueur
    full_prompt = f"Réponds en {word_limit} mots maximum :\n\n{prompt}"

    try:
        # Appel au modèle Cloud (ex: gpt-oss:120b) via le client Python officiel
        response = client.chat(
            model='gpt-oss:120b',
            messages=[{'role': 'user', 'content': full_prompt}],
            stream=False # Désactivation du streaming pour une réponse directe
        )
        
        # Retourne le contenu généré par le modèle
        return {"response": response.message.content}

    except Exception as e:
        # Gestion des erreurs de connexion ou d'authentification
        return {"error": f"Erreur avec Ollama Cloud : {str(e)}"}

# Lancement : OLLAMA_API_KEY="votre_cle" uvicorn app_cloud:app --reload