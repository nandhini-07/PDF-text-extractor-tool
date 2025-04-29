import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    # Recognize the speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand your speech.")
except sr.RequestError:
    print("Sorry, I encountered an error while trying to process your request.")

from googletrans import Translator

def translate_to_tamil(english_text):
    translator = Translator()
    translated = translator.translate(english_text, src='en', dest='ta')
    tamil_text = translated.text
    return tamil_text

english_text = text
tamil_text = translate_to_tamil(english_text)
print(tamil_text)