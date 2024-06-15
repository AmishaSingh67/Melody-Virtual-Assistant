from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import time
import os


def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        return translated_text
    except AttributeError as e:
        print("Translation error:", e)
        return None


def speak_translated_text(text, target_language):
    try:
        tts = gTTS(text=text, lang=target_language, slow=False)
        tts.save("translated_audio.mp3")
        playsound("translated_audio.mp3")
        os.remove("translated_audio.mp3")
    except Exception as e:
        print("Text to speech error:", e)


def translate_and_speak():
    print("Enter the text you want to translate:")
    text_to_translate = input("> ")

    print("Choose the language to translate into:")
    target_language = input("> ")

    translated_text = None
    retries = 3
    while not translated_text and retries > 0:  # Retry a few times
        translated_text = translate_text(text_to_translate, target_language)
        if not translated_text:
            retries -= 1
            print("Failed to translate. Retrying...")
            time.sleep(1)  # Add a small delay before retrying

    if translated_text:
        print("Translated text:", translated_text)
        speak_translated_text(translated_text, target_language)
    else:
        print("Failed to translate. Please try again later.")


# Example usage
#translate_and_speak()
