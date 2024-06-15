import PyPDF2
import pyttsx3


# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def pdf_reader():
    book_path = "C:/Users/KIIT/Desktop/java.pdf"
    with open(book_path, 'rb') as book:
        pdf_reader = PyPDF2.PdfReader(book)
        pages = len(pdf_reader.pages)
        speak(f"The PDF file has {pages} pages.")

        speak("Please enter the page number you want to read.")
        pg = int(input("Enter the page number: ")) - 1  # Adjusting index
        if pg < 0 or pg >= pages:
            speak("Invalid page number.")
            return

        page = pdf_reader.pages[pg]
        text = page.extract_text()
        speak(text)

# Assuming you have a function named `speak()` to read out the text
# If not, you need to define it or use any appropriate text-to-speech library.

#pdf_reader()
