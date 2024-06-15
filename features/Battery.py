import psutil
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_battery_info_and_suggestion():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        plugged = battery.power_plugged
        remaining_time = battery.secsleft // 60 if battery.secsleft != -1 else "Unknown"

        status = "Plugged in" if plugged else "Not plugged in"
        info = f"The battery is {percent}% charged and is currently {status}."

        # Suggestions based on battery percentage
        suggestion = ""
        if percent <= 20:
            suggestion = "You should consider charging your device soon."
        elif 20 < percent <= 50:
            suggestion = "Your battery is still good, but consider charging it to avoid running out."
        elif 50 < percent <= 80:
            suggestion = "Your battery is well-charged. Keep it up!"
        elif 80 < percent < 100:
            suggestion = "Your battery is almost fully charged."
        elif percent == 100:
            suggestion = "Your battery is fully charged. You can unplug it to preserve battery life."

        return info, suggestion
    else:
        return "Unable to retrieve battery information.", ""

# Function to speak battery information and suggestion
def speak_battery_info_and_suggestion():
    battery_info, suggestion = get_battery_info_and_suggestion()
    print(battery_info)
    speak(battery_info)
    if suggestion:
        print(suggestion)
        speak(suggestion)



#speak_battery_info_and_suggestion()

