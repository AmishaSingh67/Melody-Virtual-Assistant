import pyttsx3
import requests

# Function to fetch current temperature from OpenWeatherMap API
def get_temperature(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        return temperature
    else:
        return None

# Function to speak out the temperature
def speak_temperature(temperature, unit="Celsius"):
    engine = pyttsx3.init()
    engine.say(f"The current temperature is {temperature} degrees {unit}.")
    engine.runAndWait()

# Temperature function
def temperature():
    api_key = "9baa35380a5b8e8f57f75050bddbeb2c"
    city = "bhubaneshwar"
    temperature = get_temperature(api_key, city)
    if temperature is not None:
        speak_temperature(temperature)
    else:
        print("Failed to fetch temperature data.")

# if __name__ == "__main__":
#     temperature()
