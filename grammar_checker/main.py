import requests
import gradio as gr

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

def correct_grammar(text):
    """
    Fonction de correction appelée par l'interface Gradio.
    Utilise Llama 3.2 pour analyser et corriger le texte.
    """

    # Instruction de correction avec demande d'explications
    prompt = f"Corrige toutes les erreurs de grammaire et d'orthographe dans le texte suivant et fournis des explications:\n\n{text}"
    
    # Payload pour la requête POST
    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }

    # Envoi de la requête à Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    # Vérification du code de statut HTTP
    if response.status_code == 200:
        return response.json().get("response", "Aucune erreur corrigée")
    else:
        return f"Erreur : {response.text}"

# Configuration de l'interface graphique Gradio
interface = gr.Interface(
    fn=correct_grammar, # Fonction de traitement
    inputs=gr.Textbox(lines=5, placeholder="Entrez votre texte ici...", label="Texte à corriger"), # Entrée texte
    outputs=gr.Textbox(label="Texte corrigé & Explications"), # Sortie texte
    title="🤖 Correcteur Grammatical IA",
    description="Collez un texte avec des fautes et l'IA se chargera de le corriger tout en vous expliquant vos erreurs."
)

# Lancement de l'interface
if __name__ == "__main__" :
    interface.launch()

