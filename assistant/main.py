import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3

# URL de l'API locale d'Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

# Initialisation du moteur de synthèse vocale
engine = pyttsx3.init()

def ai_assistant(text):
    """Fonction pour interagir avec l'assistant IA en utilisant Ollama et fournir une réponse vocale."""

    prompt = f"Reponds en tant que mon assistant personnel : {text}"

    payload = {
        "model": "gpt-oss:120b-cloud",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        answer = response.json().get("response", "Aucune réponse générée")
        engine.say(answer)
        engine.runAndWait()
        return answer
    else:
        return f"Désolé, une erreur s'est produite"

def listen_command():
    recoginzer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        recoginzer.adjust_for_ambient_noise(source)
        audio = recoginzer.listen(source, language="fr-FR")

    try:
        command = recoginzer.recognize_google(audio, language="fr-FR")
        print(f"Vous avez dit : {command}")
        return command
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris.")
        return None
    except sr.RequestError as e:
        print(f"Erreur de service de reconnaissance vocale : {e}")
        return None
    
interface = gr.Interface(
    fn=ai_assistant,
    inputs=gr.Textbox(lines=5, placeholder="Entrez votre commande ici...", label="Votre commande"),
    outputs=gr.Textbox(label="Réponse de l'assistant"),
    title="🤖 Assistant Personnel IA",
    description="Entrez une commande pour votre assistant personnel IA, et il vous répondra avec une réponse vocale et textuelle."
)

if __name__ == "__main__":
    # while True:
    #     command = listen_command()
    #     if command:
    #         response = ai_assistant(command)
    #         print(f"Assistant : {response}")
    interface.launch()