import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
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


def schedule_day():
    schedule = {}

    speak("Welcome to the Day Scheduler!")
    speak("Please tell me your tasks and their corresponding times.")
    speak("You can say 'done' to finish scheduling or 'view' to see your current schedule.")

    while True:
        speak("What is your task?")
        task = takeCommand().strip()  # Change get_audio() to takeCommand()

        if task.lower() == 'done':
            break
        elif task.lower() == 'view':
            if schedule:
                speak("Your current schedule for the day is as follows:")
                for time, task in sorted(schedule.items()):
                    speak(f"At {time}, you have {task}")
            else:
                speak("No tasks scheduled for the day.")
            continue

        speak("At what time?")
        time = takeCommand().strip()  # Change get_audio() to takeCommand()
        schedule[time] = task

    if schedule:
        speak("Your final schedule for the day is as follows:")
        for time, task in sorted(schedule.items()):
            speak(f"At {time}, you have {task}")
    else:
        speak("No tasks scheduled for the day.")



#schedule_day()
