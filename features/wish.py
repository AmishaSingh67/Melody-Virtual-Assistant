import datetime
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()



# Define a function to greet the user based on the time of the day
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Boss!")
        speak("I am Your Personal Assistant Melody !!")
        speak("How Can I Help You Boss?")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss!")
        speak("I am Your Personal Assistant Melody !!")
        speak("How Can I Help You Boss?")
    else:
        speak("Good Evening Boss!")
        speak("I am Your Personal Assistant Melody !!")
        speak("How Can I Help You Boss?")

        # # Add a check to see if the pyttsx3 engine's run loop is already started
        # if not engine._inLoop:
        #     engine.runAndWait()


#wishMe()