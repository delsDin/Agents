from fastapi import FastAPI
import requests

# Initialisation de l'application FastAPI pour le chatbot
app = FastAPI()
# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/chat/")

def chatbot_response(user_input : str):
    """
    Point de terminaison API pour le chatbot.
    Envoie l'entrée de l'utilisateur à Ollama pour générer une réponse basée sur les données de l'entreprise.
    """

    # Données de l'entreprise pour le chatbot
    company_data = {
        "name": "Acme Corp",
        "description": "Une entreprise spécialisée dans les solutions technologiques innovantes.",
        "faq": [
            {"question": "Quels sont vos produits phares ?", "answer": "Nos produits phares incluent notre plateforme de gestion de projet et notre application de collaboration en équipe."},
            {"question": "Comment puis-je contacter le support ?", "answer": "Vous pouvez contacter notre support via notre site web ou par email à support@acme.com."},
            {"question": "Offrez-vous des formations ?", "answer": "Oui, nous proposons des formations en ligne et en présentiel pour nos produits."},
            {"question": "Quels sont vos horaires d'ouverture ?", "answer": "Nos bureaux sont ouverts du lundi au vendredi de 9h à 18h."}
        ]
    }
    # Simple contexte pour le chatbot
    context = f"Tu es un assistant virtuel, nommé Assiste, amical et informatif. Tu aides les utilisateurs en répondant à leurs questions et en fournissant des informations utiles basées sur les données disponibles dans {company_data}. Tu es toujours poli et tu t'efforces de fournir des réponses précises et pertinentes."
    # Instruction pour le chatbot
    prompt = f"{context}\n\nMessage de l'utilisateur :\n\n{user_input}"

    # Payload pour la requête POST
    payload = {
        "model": "gpt-oss:120b-cloud",
        "prompt": prompt,
        "stream": False
    }

    # Envoi de la requête à Ollama
    response = requests.post(OLLAMA_URL, json=payload)
    # Retourne la réponse générée ou un message d'erreur
    if response.status_code == 200:
        return response.json().get("response", "Aucune réponse générée")
    else:
        return f"Erreur : {response.text}"

# Pour lancer le serveur: uvicorn app:app --reload