import pywhatkit
import pyttsx3
import speech_recognition as sr
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return "None"


def sendMessage():
    speak("Who do you want to message")
    # recipient = input("Enter the recipient's phone number (without country code): ")
    # recipient_with_country_code = "+91" + recipient

    recipient_with_country_code = "+919835386353"

    speak("What is the message?")
    message = takeCommand()

    pywhatkit.sendwhatmsg(recipient_with_country_code, message, datetime.now().hour, datetime.now().minute + 1)
    print("Message sent successfully!")


def TaskExecution():
    while True:
        order = takeCommand()
        if "whatsapp" in order:
            sendMessage()

if __name__ == "__main__":
    TaskExecution()
