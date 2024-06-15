import pyttsx3
import speech_recognition as sr



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
            return "Ajnabee"
        query = query.lower()
        return query


chatStr = ""
def image_generation(order):
    import base64
    import os
    import requests
    import matplotlib.pyplot as plt
    from PIL import Image
    from io import BytesIO

    engine_id = "stable-diffusion-v1-6"

    response = requests.post(
        f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer sk-ajKdAFnBKMPw7u19VSKZwswCmLNLR0HV1QCrX7j5SAKSZXy4"
        },
        json={
            "text_prompts": [
                {
                    "text": f"{order}"
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        # Decode the base64 image data
        img_data = base64.b64decode(image["base64"])

        # Open the image using PIL
        img = Image.open(BytesIO(img_data))

        # Display the image
        speak("Here you go")
        img.show()



def TaskExecution():

    #wishMe()
    #speak_battery_info_and_suggestion()
    #username()


    while True:
        order = takeCommand().lower()

        if 'generate' in order:

            speak("Generating Image Please wait a moment")
            image_generation(order)

#TaskExecution()
#image_generation(order)