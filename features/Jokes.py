import pyjokes
import pyttsx3


# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)



#tellJoke()