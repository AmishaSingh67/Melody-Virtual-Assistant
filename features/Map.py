import webbrowser
import pyttsx3
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use index 1 for female voice
rate = engine.setProperty("rate", 200)  # Adjust the rate as needed

# Function to find and display a location on Google Maps
def find_location_on_map(location):
    # Construct the Google Maps URL with the location query
    maps_url = f"https://www.google.com/maps/search/?api=1&query={location}"

    # Open the URL in a web browser
    webbrowser.open(maps_url)
    speak(f"Showing {location} on Google Maps.")


# Define a function to take a command
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


# Define a function to speak out the given text
def speak(audio):
    try:
        engine.say(audio)
        print(audio)
        engine.runAndWait()
    except RuntimeError:
        pass  # Do nothing if the pyttsx3 engine's run loop is already started


# Main function to control the flow of the program
def TaskExecution():
    #wishMe()
    while True:
        order = takeCommand().lower()

        if 'where is' in order:
            location = order.replace('where is', '').strip()
            find_location_on_map(location)
            speak(f"Showing {location} on Google Maps.")  # Speak the response
            continue  # Skip to the next iteration after handling the command
        # Add other commands and functionalities here...

#
# if __name__ == '__main__':
#     # Add other initialization code here...
#     TaskExecution()
