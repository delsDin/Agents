import os
from fastapi import FastAPI
from ollama import Client

# Initialisation de l'application FastAPI pour l'extracteur NER
app = FastAPI()

# Configuration du client Ollama pour une utilisation via une instance distante ou Cloud
# La clé API est récupérée de manière sécurisée via une variable d'environnement
client = Client(
    host='https://ollama.com',
    headers={'Authorization': f"Bearer {os.environ.get('OLLAMA_API_KEY')}"}
)

@app.post("/ner/")
def generate_text(text: str):
    """
    Point de terminaison pour l'extraction via le SDK Ollama Cloud.
    Utilise des modèles plus massifs pour une meilleure précision d'extraction.
    """
    
    # Construction du prompt demandant une extraction précise
    full_prompt = f"Extrait toutes les entités nommées (personnes, organisations, lieu, monnaie, quantité, dates) s'ils y en a avec une liste à puces du texte suivant :\n\n{text}"

    try:
        # Appel au modèle Cloud (ex: gpt-oss:120b) via le client Python officiel
        response = client.chat(
            model='gpt-oss:120b',
            messages=[{'role': 'user', 'content': full_prompt}],
            stream=False # Réception directe de la réponse
        )
        
        # Retourne le contenu extrait par le modèle
        return {"response": response.message.content}

    except Exception as e:
        # Gestion des erreurs d'authentification ou de réseau
        return {"error": f"Erreur avec Ollama Cloud : {str(e)}"}

# Lancement : OLLAMA_API_KEY="votre_cle" uvicorn app_cloud:app --reload