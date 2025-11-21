# TTS-Translator — English Text Translator & Text-to-Speech (Python)

EchoLang is a Python-based command-line tool that translates English text into other languages and converts the translated text into spoken audio.
It supports Hindi, Spanish, French, and German, using Hugging Face translation models and gTTS for text-to-speech.

# Features

• Translate English → Hindi / Spanish / French / German
• Listen to the translated output using gTTS + pygame
• Supports multiple languages
• Clean & interactive command-line interface
• Auto-generated temporary audio files
• Easy to extend with more languages

# Technologies Used

• Python
• Transformers (Hugging Face)
• gTTS (Google Text-to-Speech)
• pygame
• time, os, sys

# Installation
1️⃣ Clone the repository
git clone https://github.com/Anshikam0905/TTS-Translator.git
cd TTS-Translator

2️⃣ Install dependencies
pip install transformers gtts pygame

If needed:
pip install torch

# How to Run

Run the program using: <br>
<b> python echolang.py </b>

• Supported Languages
The following translation/speech languages are supported:

Code	Language
hi	Hindi
es	Spanish
fr	French
de	German

Example:
Enter target language code (hi/es/fr/de): es
You: I love programming
Spanish: Me encanta programar
(Speaking…)
