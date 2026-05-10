import requests
import gradio as gr

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
def chatbot_response(user_input):
    """
    Fonction de traitement appelée par l'interface Gradio.
    Utilise ollama pour générer une réponse basée sur l'entrée de l'utilisateur.
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

    # Vérification du code de statut HTTP
    if response.status_code == 200:
        return response.json().get("response", "Aucune réponse générée")
    else:
        return f"Erreur : {response.text}"
    

# Configuration de l'interface graphique Gradio
interface = gr.Interface(
    fn=chatbot_response, # Fonction de traitement
    inputs=gr.Textbox(lines=5, placeholder="Posez votre question ici...", label="Votre question"), # Entrée texte
    outputs=gr.Textbox(label="Réponse du chatbot"), # Sortie texte
    title="🤖 Chatbot IA pour Acme Corp",
    description="Posez une question sur Acme Corp et notre chatbot IA vous fournira une réponse informative basée sur les données de l'entreprise."
)

# Lancement de l'interface
if __name__ == "__main__":
    interface.launch()