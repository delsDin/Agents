import requests  # Bibliothèque pour envoyer des requêtes HTTP
import gradio as gr  # Bibliothèque pour créer des interfaces graphiques

# Définition de l'URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"  # URL de l'API

def extract_named_entities(text):
    """
    Fonction pour extraire les entités nommées (personnes, organisations, lieu, monnaie, quantité, dates) 
    à partir d'un texte donné en utilisant l'Outils de Reconnaisance d'Entité Nommées.
    
    Parameters:
    text (str): Le texte à partir duquel extraire les entités nommées.
    
    Returns:
    str: Les entités nommées extraites du texte.
    """

    # Prompt optimisé pour une extraction structurée et précise
    prompt = (
        "Tu es un expert en extraction d'entités nommées. Analyse le texte ci-dessous et extrait "
        "UNIQUEMENT les entités suivantes : PERSONNE, ORGANISATION, LIEU, DATE, MONNAIE, QUANTITÉ.\n\n"
        "Règles :\n"
        "1. Présente le résultat sous forme de liste à puces classée par catégorie.\n"
        "2. Ne fais aucun commentaire supplémentaire.\n"
        "3. Si aucune entité n'est trouvée, réponds : 'Aucune entité détectée.'\n\n"
        f"Texte à analyser :\n{text}"
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
    fn=extract_named_entities,  # Fonction de traitement à utiliser
    inputs=gr.Textbox(lines=5, placeholder="Entrez votre texte ici...", label="Texte"),  # Entrée texte
    outputs=gr.Textbox(label="Entités extraites"),  # Sortie texte
    title=" Extracteur NER",  # Titre de l'interface
    description="Mettez le texte et l'IA se chargera d'extraire les personnes, organisations, localisations et dates"  # Description de l'interface
)

# Lancement de l'interface graphique
if __name__ == "__main__":
    interface.launch()
