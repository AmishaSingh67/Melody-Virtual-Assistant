import datetime #
import os #
import random #
import sys #
import time #
import webbrowser #
import pyautogui
import pyttsx3 #
import pywhatkit
import speech_recognition as sr #
from features.Alarm import setAlarm
from features.Battery import get_battery_info_and_suggestion, speak_battery_info_and_suggestion
from features.Gemini import chat
from features.Image_Generator import image_generation
from features.Jokes import tellJoke
# from features.News import getCurrentNews
# from features.PDF_Reading import pdf_reader
from features.VoiceChanger_M_F import change_voice_to_female, change_voice_to_male
from features.game import game_play
from features.location import find_location
from features.theme import set_theme_mode
from features.weather import getWeatherReport
from features.wikipedia import searchWikipedia
from features.wish import wishMe
from features.Whatsapp import sendMessage
from features.Temperature import temperature
from features.Map import find_location_on_map
from features.Calculator import calculator
from features.UserName import username
from features.Terminal_clear import clear_screen, clear_previous_chats
# from features.Translator import translate_and_speak
# from features.Scheduler import schedule_day




# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use index 1 for female voice
rate = engine.setProperty("rate", 200)  # Adjust the rate as needed

# Define a function to speak out the given text
def speak(audio):
    try:
        engine.say(audio)
        print(audio)
        engine.runAndWait()
    except RuntimeError:
        pass  # Do nothing if the pyttsx3 engine's run loop is already started

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


# SHUT DOWN , RESTART , HIBERNATE FUNCTIONS
def confirm_action(action):  # action is the action to confirm (shutdown, restart, or hibernate)
    speak(f"Are you sure you want to {action} the computer?")
    confirm = takeCommand().lower()
    if 'order' in confirm:
        speak("Confirming your request in Seconds.")
        speak("5 4 3 2 1 0 ")
        speak("Now See The Magic... ")
        time.sleep(4)
        if action == 'shutdown':
            os.system("shutdown /s /t 1")
        elif action == 'restart':
            os.system("shutdown /r /t 1")
        elif action == 'hibernate':
            os.system("shutdown /h")
    else:
        speak(f"{action.capitalize()} canceled.")






# Main function to control the flow of the program
def TaskExecution():

    wishMe()
    #speak_battery_info_and_suggestion()
    #username()


    while True:
        order = takeCommand().lower()

        if order.strip() == "":
            continue  # Skip to the next iteration if the order is empty

################################################################
        if 'how are you' in order:
            speak("I am fine, Thank you.")
            speak("How are you, Boss?")

        elif 'fine' in order or 'good' in order:
            speak("It's good to know that you are fine.")

        elif 'who i am' in order:
            speak('if you can talk then surely you are a human.')

        elif 'love' in order:
            speak('it is the 7th sense that destroy all other senses')

        elif 'who are you' in order:
            speak('I am your virtual assistant Jarvis GirlFriend.')

        elif 'i love you' in order:
            speak('Oh my god, thank you. I love you too. Anything I can help you with?')

        elif 'will you be my girlfriend' in order or 'will you be my valentine' in order:
            speak("Sorry I am in situtionship.")

        elif 'what is your name' in order:
            speak("my friends call me Melody !!")
###########################################################################

        elif 'open notepad' in order:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            speak("notepad is open")
        elif 'close notepad' in order:
            os.system("taskkill /im notepad.exe /f")
            speak("Notepad is closed")

        elif 'open chrome' in order:
            cpath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            os.startfile(cpath)
            speak("chrome is open")
        elif  'close chrome' in order:
            os.system("taskkill /im chrome.exe /f")
            speak("chrome is closed")

        elif 'open file' in order:
            fpath = "C:/Windows/explorer.exe"
            os.startfile(fpath)
            speak("File Explorer is open")
        elif 'close file' in order:
            os.system("taskkill /im explorer.exe /f")
            speak("File Explorer is closed")

        elif 'open cmd' in order:
            mpath = "C:/Windows/System32/cmd.exe"
            os.startfile(mpath)
            speak("Command Prompt is open")
        elif 'close cmd' in order:
            os.system("taskkill /im cmd.exe /f")
            speak("Command Prompt is closed")

        elif 'open pycharm' in order:
            ppath = "C:/Program Files/JetBrains/PyCharm 2023.3.4/bin/pycharm64.exe"
            os.startfile(ppath)
            speak("PyCharm is open")
        elif 'close pycharm' in order:
            os.system("taskkill /im pycharm64.exe /f")
            speak("PyCharm is closed")


        elif 'play music' in order or 'play songs' in order:
            music_dir = "D:\\Songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("playing music")

        elif 'open stackoverflow' in order:
            webbrowser.open("https://stackoverflow.com")
            speak("Stack Overflow is open")

        elif 'open github' in order:
            webbrowser.open("https://github.com")
            speak("GitHub is open")

        elif 'open google' in order:
            webbrowser.open("https://www.google.com")
            speak("Google is open")

        elif 'open youtube' in order:
            webbrowser.open("https://www.youtube.com")
            speak("YouTube is open")

        elif 'open facebook' in order:
            webbrowser.open("https://www.facebook.com")
            speak("Facebook is open")

        elif 'open instagram' in order:
            webbrowser.open("https://www.instagram.com")
            speak("Instagram is open")

        elif 'open linkedin' in order:
            webbrowser.open("https://www.linkedin.com")
            speak("LinkedIn is open")

        elif 'open twitter' in order:
            webbrowser.open("https://twitter.com")
            speak("Twitter is open")

        elif 'open whatsapp web' in order:
            webbrowser.open("https://web.whatsapp.com")
            speak("WhatsApp is open")

        elif 'open telegram' in order:
            webbrowser.open("https://web.telegram.org/k/")
            speak("Telegram is open")


        elif 'close window' in order or 'close browser ' in order or 'close' in order:
            os.system("taskkill /im chrome.exe /f")  # Change 'chrome.exe' to the appropriate browser process if needed
            speak("Window is closed")

        elif "send an email" in order:
            speak("On what email address do you want to send sir?. Please enter in the terminal")
            receiver_add = input("Email address:")
            speak("What should be the subject sir?")
            subject = take_command().capitalize()
            speak("What is the message ?")
            message = take_command().capitalize()
            if send_email(receiver_add, subject, message):
                speak("I have sent the email sir")
                print("I have sent the email sir")
            else:
                speak("something went wrong Please check the error log")


        elif 'search youtube for' in order:
            query = order.replace('search youtube for', '').strip()
            query = query.replace(' ', '+')  # Replace spaces with '+' for URL
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(search_url)
            speak("Here are the search results on YouTube")
            pywhatkit.playonyt(query)

        elif 'search google for' in order:
            query = order.replace('search google for', '').strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            speak("Here are the search results on Google")

        elif 'search wikipedia for' in order:
            order = order.replace('search wikipedia for', '').strip()
            searchWikipedia(order)

        elif 'weather report' in order:
            getWeatherReport()

        elif 'Temperature' in order:
            temperature()

        elif 'where is' in order:
            location = order.replace('where is', '').strip()
            find_location_on_map(location)
            #speak(f"Showing {location} on Google Maps.")  # Speak the response
            continue

        elif 'current news' in order or 'news' in order:
            getCurrentNews()

        elif 'calculate' in order:
            calculator()

        elif 'what is the time' in order or 'time' in order:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif 'what is the date' in order or 'date' in order:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"The current date is {current_date}")

        elif 'take a screenshot' in order:
            speak("Taking a screenshot...")
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved as screenshot.png")
            speak("Here is your screenshot:")

        elif "click my photo" in order:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        # Add 'set alarm' functionality to the main loop
        elif 'set alarm' in order or 'wake me up' in order:
            setAlarm()


        elif 'shutdown' in order:
            confirm_action('shutdown')

        elif 'restart' in order:
            confirm_action('restart')

        elif 'hibernate' in order:
            confirm_action('hibernate')

        # Add functionality to the main loop
        elif 'tell a joke' in order or 'joke' in order:
            tellJoke()

        # Add commands to change the voice
        elif 'change voice to male' in order or 'change male' in order:
            change_voice_to_male()
        elif 'change voice to female' in order or 'change female' in order:
            change_voice_to_female()


            # Speak battery percentage on command
        elif 'battery percentage' in order or 'battery' in order:
            get_battery_info_and_suggestion()
            speak_battery_info_and_suggestion()

        elif 'internet speed' in order:
            try:
                speak("Boss just wait second i will show you the speeds...")
                os.system('cmd /k "speedtest"')

            except:
                speak("Sorry Boss, I am unable to check internet speed")
                sys.exit()

                # SECOND METHOD

            # st=speedtest.Speedtest()
            # dl=st.download()
            # ul=st.upload()
            # speak(f"Boss we have {dl} bit per second for download and {ul} bit per second for upload")

        elif 'volume up' in order or 'increase volume' in order:
            pyautogui.press('volumeup')
            speak("Volume increased")

        elif 'volume down' in order or 'decrease volume' in order:
            pyautogui.press('volumedown')
            speak("Volume decreased")

        elif 'mute' in order or 'silence' in order:
            pyautogui.press('volumemute')
            speak("Volume muted")

        elif 'read pdf' in order:
            speak("Sure, I'll open the PDF file.")
            pdf_reader()

        elif 'Translate' in order:
            speak("Sure, I'll translate the text.")
            translate_and_speak()


        elif 'take a picture' in order:
            speak("Sure, I'll open the camera for you. Please take the picture.")
            take_picture()
            speak("Picture taken. And save in the file.")

        elif 'location' in order:
            speak("Sure, I'll find your location.")
            location_info = find_location()
            speak(location_info)

        elif 'change theme' in order:
            set_theme_mode()

        elif "play a game" in order:
            game_play()

        elif "open" in order:  # EASY METHOD
            query = order.replace("open", "")
            query = query.replace("jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'whatsapp' in order:
            sendMessage()


        elif 'schedule' in order:
            schedule_day()

        elif "clear screen" in order or "reset" in order:
            clear_screen()
            clear_previous_chats()
            speak("Screen cleared")

        elif 'generate' in order:
            speak("Generating Image Please wait a moment")
            image_generation(order)



        elif 'break' in order or 'stop' in order or 'get lost' in order or 'exit' in order:
            speak("Goodbye Boss And GetLost, I Am Going to Sleep Now...")
            speak("Wake Me Up If You Need Me.!")
            sys.exit()

        else:
            print("Chatting...")
            chat(order)




if __name__ == '__main__':
    run_counter = 1  # Initialize a counter to keep track of the number of runs
    while True:
        permission = takeCommand().lower()
        if "start" in permission or "wake up" in permission or "melody" in permission or "hey" in permission:
            TaskExecution()
            folder_path = "C:/Users/KIIT/PycharmProjects/pythonProject/output_logs"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Get current date and time
            file_name = os.path.join(folder_path,f"output_{timestamp}_{run_counter}.txt")  # Use timestamp and run_counter
            with open(file_name, 'w') as f:
                original_stdout = sys.stdout
                sys.stdout = f
                TaskExecution()
                sys.stdout = original_stdout
            run_counter += 1  # Increment the counter for the next run
        elif "sleep now" in permission:
            speak("Goodbye Boss And GetLost, I Am Going to Sleep Now...")
            speak("Wake Me Up If You Need Me.!")
            break
















