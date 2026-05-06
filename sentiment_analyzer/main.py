import requests
import gradio as gr

# Définition de l'URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"  # URL de l'API

def sentiment_analyzer(text):
    """
    """

    prompt = (
        f"Tu es un expert en analyse de sentiment. Donne un score /10 du texte suivant :\n\n{text}"
    )
    
    # Définition du payload pour la requête POST à l'API d'Ollama
    payload = {
        "model": "llama3.2:1b",  # Modèle d'IA à utiliser
        "prompt": prompt,  # Prompt pour la requête
        "stream": False  # Option pour la requête
    }

    # Envoi de la requête POST à l'API d'Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    # Vérification du code de statut HTTP de la réponse
    if response.status_code == 200:  # Code de statut 200 : requête réussie
        # Récupération de la réponse de l'API
        return response.json().get("response", "Aucune erreur corrigée")
    else:  # Code de statut différent de 200 : requête en échec
        # Renvoi d'un message d'erreur
        return f"Erreur : {response.text}"

# Création d'une interface graphique pour l'extraction des entités nommées
interface = gr.Interface(
    fn=sentiment_analyzer,  # Fonction de traitement à utiliser
    inputs=gr.Textbox(lines=5, placeholder="Entrez votre texte ici...", label="Texte"),  # Entrée texte
    outputs=gr.Textbox(label="Score"),  # Sortie texte
    title="Analyseur de sentiment",  # Titre de l'interface
    description="Mettez le texte et l'IA l'analysera et donnera le score de satisfation ou de joie"
)

# Lancement de l'interface graphique
if __name__ == "__main__":
    interface.launch()
