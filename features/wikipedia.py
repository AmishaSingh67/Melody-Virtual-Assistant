import wikipedia
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception:
            speak("Unable to recognize your voice...")
            return "none"

def searchWikipedia(query):
    try:
        result = wikipedia.summary(query)
        speak("According to Wikipedia:")
        speak(result)
    except wikipedia.DisambiguationError:
        speak("There are multiple possible matches, please be more specific.")
    except wikipedia.PageError:
        speak("Sorry, no information found on Wikipedia for the given topic.")
    except Exception as e:
        speak(f"An error occurred: {e}")

def TaskExecution():
    while True:
        order = takeCommand()
        if 'wikipedia' in order:
            searchWikipedia(order.replace('wikipedia', '').strip())

if __name__ == "__main__":
    TaskExecution()
