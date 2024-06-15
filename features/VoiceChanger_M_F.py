import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice

# Define a function to speak out the given text
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#Function to change the voice to male
def change_voice_to_male():
    global engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Use index 0 for male voice
    speak("Voice changed to male.")

# Function to change the voice to female
def change_voice_to_female():
    global engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice
    speak("Voice changed to female.")


#change_voice_to_male()

#change_voice_to_female()