# 🎙️ Assistant Personnel Vocal (assistant)

Cet agent est un assistant personnel intelligent capable de comprendre des commandes textuelles (et potentiellement vocales) et de répondre à la fois par écrit et par synthèse vocale.

## 🚀 Fonctionnalités
- **Interaction Multimodale** : Supporte les commandes textuelles via une interface web et possède les bases pour la reconnaissance vocale.
- **Synthèse Vocale (TTS)** : L'assistant répond oralement grâce à la bibliothèque `pyttsx3`.
- **Reconnaissance Vocale (STT)** : Intègre `speech_recognition` pour écouter les commandes de l'utilisateur (français supporté).
- **Interface Gradio** : Une interface conviviale pour interagir avec l'assistant.

## 🛠️ Technologies
- **Frameworks** : Gradio
- **IA/LLM** : `gpt-oss:120b-cloud` (via Ollama)
- **Audio** : `speech_recognition` (STT), `pyttsx3` (TTS)
- **Langage** : Python

## 📁 Structure du projet
- `main.py` : Script principal gérant l'interface Gradio, la synthèse vocale et la logique de l'assistant.

## ⚙️ Installation & Utilisation

### 1. Installation des dépendances
Vous aurez besoin de bibliothèques supplémentaires pour l'audio :
```bash
pip install requests gradio speech_recognition pyttsx3 PyAudio
```
*Note : `PyAudio` peut nécessiter des dépendances système supplémentaires (comme `portaudio`).*

### 2. Lancement
Pour démarrer l'assistant avec l'interface web :
```bash
python main.py
```

## 📝 Fonctionnement
L'assistant prend une entrée utilisateur, l'envoie au modèle LLM local, puis utilise le moteur de synthèse vocale pour "dire" la réponse tout en l'affichant dans l'interface Gradio. Le code inclut également une fonction `listen_command()` pour une utilisation future en mode mains libres via microphone.
