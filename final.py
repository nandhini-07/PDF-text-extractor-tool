import docx
import PyPDF2
from PIL import Image
from pytesseract import pytesseract
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
def extract_text_from_docx(docx_path):
    try:
        text = ""
        doc = docx.Document(docx_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print("Error:", e)

def extract_text_from_pdf(pdf_file_path):
    text = ""
    
    try:
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            for page_num in range(len(pdf_reader.pages) ):
                page = pdf_reader.pages[page_num]               
                text += page.extract_text()
    except Exception as e:
        print("Error:", e)
    
    return text


def translate(examine_text,lan1,lan2):
    translator = Translator()
    translated = translator.translate(examine_text, src=lan1, dest=lan2)
    translate_text = translated.text
    return translate_text

def voice(mytext,lan):
    myobj = gTTS(text=mytext, lang=lan, slow=False)
    myobj.save("speech.mp3")
    os.system("speech.mp3")

def voiceinput(la1,la2):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text1 = recognizer.recognize_google(audio)
        print("You said:", text1)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
    except sr.RequestError:
        print("Sorry, I encountered an error while trying to process your request.")
    new_text=translate(text1,la1,la2)
    print(new_text)
    voice(new_text,la2)


def extract_text_from_image(image_path):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract"
    pytesseract.tesseract_cmd = path_to_tesseract
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)

print("main menu")
print("1.Voice input")
print("2.PDF")
print("3.Document")
print("4.Image")
ch=input("enter the choice")
if(ch=='1'):
    src=input("enter the source language :")
    des=input("enter the destination language :")
    voiceinput(src,des)
elif(ch=='2'):
    pdf_path = input("enter the pdf name:")
    extracted_text = extract_text_from_pdf(pdf_path)
    if extracted_text:
        src=input("enter the source language :")
        des=input("enter the destination language :")
        translate_text = translate(extracted_text,src,des)
        print(translate_text)
        voice(translate_text,des)
    else:
        print("No Such File Exixts")

elif(ch=='3'):
    docx_path = input("enter the file name:")
    docx_text = extract_text_from_docx(docx_path)
    if docx_text:
        src=input("enter the source language :")
        des=input("enter the destination language :")
        translate_text = translate(docx_text,src,des)
        print(translate_text)
        voice(translate_text,des)
    else:
        print("No Such File Exixts")

elif(ch=='4'):
    
    image_path = input("enter the image file name:")
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text From Image:")
    #print(extracted_text)
    if extracted_text:
        src=input("enter the source language :")
        des=input("enter the destination language :")
        print("Extracted Text From Image:")
        translate_text = translate(extracted_text,src,des)
        print(translate_text)
        voice(translate_text,des)
    else:
        print("No Such File Exixts")


