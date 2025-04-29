import docx
from googletrans import Translator
def extract_text_from_docx(docx_path):
    try:
        text = ""
        doc = docx.Document(docx_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print("Error:", e)

        
def translate_to_tamil(english_text,lan1,lan2):
    translator = Translator()
    translated = translator.translate(english_text, src=lan1, dest=lan2)
    tamil_text = translated.text
    return tamil_text


docx_path = input("enter the file:")
docx_text = extract_text_from_docx(docx_path)
src=input("enter the source language :")
des=input("enter the destination language :")
tamil_text = translate_to_tamil(docx_text,src,des)
print(tamil_text)

