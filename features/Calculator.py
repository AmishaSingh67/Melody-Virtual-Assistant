import pyttsx3
import speech_recognition as sr

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    # Adjust recognizer settings
    r.energy_threshold = 2000  # Adjust energy threshold as needed (lower values make it more sensitive)
    r.pause_threshold = 0.5  # Adjust pause threshold as needed (lower values detect shorter pauses)
    r.non_speaking_duration = 0.2  # Adjust non-speaking duration as needed
    r.dynamic_energy_threshold = True  # Enable dynamic energy threshold

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.3
        audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Adjust timeout and phrase time limit
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
            query = query.lower()
            return query
        except sr.UnknownValueError:
            print("Unable to recognize your voice...")
            return ""
        except sr.RequestError:
            print("I'm sorry, I'm having trouble accessing the Google API.")
            return ""


def calculator():
    speak("What do you want to calculate?")
    equation = takeCommand()
    try:
        result = eval(equation)
        speak(f"The result is {result}")
    except Exception as e:
        speak("Sorry, I couldn't calculate that.")
        print(e)
    speak("Do you want to calculate again?")
    again = takeCommand().lower()
    if 'yes' in again:
        calculator()
    else:
        speak("Thank you for using the calculator.")
        speak("Do you want to do anything else?")
        action = takeCommand().lower()
        if 'yes' in action:
            TaskExecution()
        else:
            speak("Goodbye!")
            # Exit the program after the user is done with the calculator
    return result  # Return the result for testing purposes
