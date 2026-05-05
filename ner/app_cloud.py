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
    
    # Prompt optimisé pour une extraction structurée et précise via le Cloud
    full_prompt = (
        "Tu es un expert en extraction d'entités nommées. Analyse le texte ci-dessous et extrait "
        "UNIQUEMENT les entités suivantes : PERSONNE, ORGANISATION, LIEU, DATE, MONNAIE, QUANTITÉ.\n\n"
        "Règles :\n"
        "1. Présente le résultat sous forme de liste à puces classée par catégorie.\n"
        "2. Ne fais aucun commentaire supplémentaire.\n"
        "3. Si aucune entité n'est trouvée, réponds : 'Aucune entité détectée.'\n\n"
        f"Texte à analyser :\n{text}"
    )

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