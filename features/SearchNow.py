import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice

# Define a function to speak out the given text
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    # Adjust recognizer settings
    r.energy_threshold = 4000  # Adjust energy threshold as needed
    r.dynamic_energy_threshold = True  # Enable dynamic energy threshold

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Adjust timeout and phrase time limit
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
        except Exception as e:
            speak("Unable to recognize your voice...")
            return "none"
        query = query.lower()
        return query

def searchGoogle(order):
    if "google" in order:
        import wikipedia as googleScrap
        order = order.replace("jarvis","")
        order = order.replace("google search","")
        order = order.replace("google","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(order)
            result = googleScrap.summary(order,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(order):


    if "youtube" in order:
        speak("This is what i found for your search!")
        order = order.replace("youtube search","")
        order = order.replace("youtube","")
        order = order.replace("jarvis","")
        web = "https://www.youtube.com/results?search_order=" + order
        webbrowser.open(web)
        pywhatkit.playonyt(order)
        speak("Done, Sir")

def searchWikipedia(order):
    if "wikipedia" in order:
        speak("Searching from wikipedia....")
        order = order.replace("wikipedia","")
        order = order.replace("search wikipedia","")
        order = order.replace("jarvis","")
        Results = wikipedia.summary(order,sentences = 2)
        speak("According to wikipedia..")
        print(Results)
        speak(Results)

def TaskExecution():

    #wishMe()
    #speak_battery_info_and_suggestion()
    #username()


    while True:
        order = takeCommand().lower()

        import pywhatkit

        if 'search youtube for' in order:
            query = order.replace('search youtube for', '').strip()
            query = query.replace(' ', '+')  # Replace spaces with '+' for URL
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(search_url)
            speak("Here are the search results on YouTube")
            pywhatkit.playonyt(query)



        elif 'search google for' in order:
            order = order.replace('search google for', '').strip()
            search_url = f"https://www.google.com/search?q={order}"
            webbrowser.open(search_url)
            speak("Here are the search results on Google")

if __name__ == "__main__":
    TaskExecution()