import requests
import gradio as gr

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, word_limit=100):
    """
    Fonction pour générer un texte via l'API Ollama.
    Cette fonction est appelée par l'interface Gradio.
    """

    # Formatage du prompt pour inclure la limite de mots
    full_prompt = f"Génère une reponse avec {word_limit} mots :\n\n{prompt}"
    
    # Paramètres de la requête
    payload = {
        "model": "llama3.2:1b",
        "prompt": full_prompt,
        "stream": False # Réception de la réponse en un seul bloc
    }

    try:
        # Envoi de la requête à l'API locale d'Ollama
        response = requests.post(OLLAMA_URL, json=payload)

        # Vérification du succès de la requête
        if response.status_code == 200:
            return response.json().get("response", "Contenu non généré.")
        else:
            return f"Erreur : {response.text}"
    except Exception as e:
        return f"Erreur de connexion : {str(e)}"

# Création de l'interface utilisateur avec Gradio
interface = gr.Interface(
    fn=generate_text, # Fonction de traitement
    inputs=[
        gr.Textbox(lines=3, placeholder="Entrez votre prompt ici", label="Prompt"), # Zone de texte
        gr.Slider(50, 500, step=50, label="Nombre de mots") # Curseur pour la longueur
    ],
    outputs=gr.Textbox(label="Résultat de la génération"), # Zone d'affichage du résultat
    title="Générateur de Texte IA",
    description="Une interface simple pour générer du contenu textuel en utilisant Llama 3.2 via Ollama."
)

# Lancement de l'application
if __name__ == "__main__":
    interface.launch()