from googletrans import Translator

def translate_to_tamil(english_text):
    translator = Translator()
    translated = translator.translate(english_text, src='en', dest='ta')
    tamil_text = translated.text
    return tamil_text

english_text =input("Enter the text")
tamil_text = translate_to_tamil(english_text)
print(tamil_text)
