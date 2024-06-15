from newsapi import NewsApiClient #pip install newsapi-python
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def getCurrentNews():
    api_key = '7f1b0e0e8ff34b5b85f5a702105e9e98'  # Replace 'YOUR_API_KEY_HERE' with your actual News API key
    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(language='en', country='in')  # Adjust language and country as needed
    articles = top_headlines['articles']
    if articles:
        speak("Here are the top news headlines:")
        for index, article in enumerate(articles[:2]):
            title = article['title']
            speak(f"News {index + 1}: {title}")
    else:
        speak("Sorry, I couldn't fetch the current news at the moment.")

#getCurrentNews()