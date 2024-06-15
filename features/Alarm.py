import datetime
import time
import pyttsx3


# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def setAlarm():
    speak("At what time would you like to set the alarm?")
    speak("Please specify the time as hours, minutes, and AM or PM.")

    # Taking input from the user
    alarm_time_str = input("Enter the time as hours, minutes, and AM/PM (Example., 07:30 AM) : ").strip().lower()

    try:
        # Try parsing time with different formats
        alarm_time = None
        formats = ["%I:%M %p", "%I:%M%p"]
        for fmt in formats:
            try:
                alarm_time = datetime.datetime.strptime(alarm_time_str, fmt)
                break
            except ValueError:
                continue

        if alarm_time:
            speak(f"Alarm set for {alarm_time.strftime('%I:%M %p')}.")
            while True:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                if current_time == alarm_time.strftime("%I:%M %p"):
                    speak("Alarm! Alarm! Wake up!")
                    break
                # Check every 10 seconds
                time.sleep(10)
        else:
            raise ValueError
    except ValueError:
        speak("Sorry, I didn't understand the time. Please try again.")


#setAlarm()