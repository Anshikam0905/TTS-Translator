
from transformers import pipeline
from gtts import gTTS
import pygame
import os
import sys
import time

# Supported translation and speech languages
SUPPORTED_LANGUAGES = {
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
}

def display_language_options():
    print("EchoLang — Translate English to Speech (Windows)")
    print("Supported languages:")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"  {code} → {name}")

def get_language_choice():
    lang_code = input("\nEnter target language code (hi/es/fr/de): ").strip().lower()
    if lang_code not in SUPPORTED_LANGUAGES:
        print("Invalid language code. Exiting.")
        sys.exit(1)
    return lang_code

def load_translation_model(lang_code):
    model_name = f"Helsinki-NLP/opus-mt-en-{lang_code}"
    return pipeline(f"translation_en_to_{lang_code}", model=model_name)

def translate_text(translator, text):
    result = translator(text)
    return result[0]['translation_text']

def speak_text(text, lang_code):
    try:
        # Create a unique filename for each audio to avoid overwriting issues
        timestamp = str(int(time.time()))
        audio_file = f"translated_{timestamp}.mp3"

        # Convert text to speech and save
        tts = gTTS(text=text, lang=lang_code)
        tts.save(audio_file)

        # Play audio using pygame
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        print(" Speaking...")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Clean up: stop music and delete the audio file
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        os.remove(audio_file)

    except Exception as e:
        print(f" Error playing audio: {e}")
        print(f" Audio saved as {audio_file}. Please play it manually.")

def main():
    display_language_options()
    lang_code = get_language_choice()
    translator = load_translation_model(lang_code)

    print("\n Type English text to translate (type 'quit' to exit):")
    while True:
        text_en = input("You: ").strip()
        if text_en.lower() in ['quit', 'exit']:
            print(" Exiting EchoLang. Goodbye!")
            break

        translated_text = translate_text(translator, text_en)
        print(f"{SUPPORTED_LANGUAGES[lang_code]}: {translated_text}")
        speak_text(translated_text, lang_code)

if __name__ == "__main__":
    main()
