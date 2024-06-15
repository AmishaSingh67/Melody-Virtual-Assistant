import pyttsx3
import requests
import speech_recognition as sr

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        speak("Please say the name of the city.")
        print("Listening...")  # Print listening message
        audio = r.listen(source, timeout=5)  # Set timeout to 5 seconds

    try:
        print("Recognizing...")  # Print recognizing message
        city_name = r.recognize_google(audio)
        print(f"Recognized text: {city_name}")  # Print recognized text
        return city_name
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        speak("Sorry, I couldn't process your request. Please try again later.")
    return None


def getWeatherReport():
    while True:
        city_name = recognize_speech()
        if city_name:
            api_key = "9baa35380a5b8e8f57f75050bddbeb2c"
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            response = requests.get(base_url)
            data = response.json()
            if data.get("cod") == 200:
                try:
                    weather_description = data["weather"][0]["description"]
                    temperature = data["main"]["temp"]
                    humidity = data["main"]["humidity"]
                    wind_speed = data["wind"]["speed"]
                    speak(f"The current weather in {city_name} is {weather_description}.")
                    speak(f"The temperature is {temperature} degrees Celsius.")
                    speak(f"The humidity is {humidity}%.")
                    speak(f"The wind speed is {wind_speed} meters per second.")
                    break  # Exit the loop if weather data is successfully retrieved
                except KeyError:
                    speak("Error: Weather data not available for the specified location.")
            else:
                speak("City not found or weather data unavailable.")



if __name__ == "__main__":
    getWeatherReport()  # Call the function to start the process
