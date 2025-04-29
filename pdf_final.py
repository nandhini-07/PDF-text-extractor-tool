import PyPDF2
import pyttsx3
import vpython
from  vpython import *
from googletrans import *
import Translator
import docx
import PyPDF2

def extract_text_from_docx(docx_path):
    text = ""
    try:
        doc = docx.Document(docx_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print("Error:", e)
    return text
def main():
    docx_path = "solarsystem.docx"
    docx_text = extract_text_from_docx(docx_path)
    print("Text extracted from DOCX:")
    print(docx_text)

    
if __name__ == "__main__":
    main()



def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    return text

pdf_path = "sample.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
a=extracted_text
print(a)



def translate_to_tamil(english_text):
    translator = Translator()
    translated = translator.translate(english_text, src='en', dest='ta')
    tamil_text = translated.text
    return tamil_text

english_text =a
tamil_text = translate_to_tamil(english_text)
print(tamil_text)


text=pyttsx3.init()
ans=a 
text.say(ans)
text.runAndWait()



# Function to create a planet
def create_planet(pos, radius, color):
    return sphere(pos=pos, radius=radius, color=color)

# Function to create an orbit path
def create_orbit(pos):
    return curve(pos=[pos, pos])

# Create a 3D scene
scene = canvas(title='Solar System')

# Create the Sun
sun = sphere(pos=vector(0, 0, 0), radius=10, color=color.yellow)

# Create the planets
planets = [
    create_planet(pos=vector(0.39, 0, 0), radius=0.04, color=color.gray(0.7)),
    create_planet(pos=vector(0.72, 0, 0), radius=0.1, color=color.orange),
    create_planet(pos=vector(1, 0, 0), radius=0.1, color=color.blue),
    create_planet(pos=vector(1.52, 0, 0), radius=0.08, color=color.red),
    create_planet(pos=vector(5.2, 0, 0), radius=0.5, color=color.orange),
    create_planet(pos=vector(9.54, 0, 0), radius=0.4, color=color.orange),
    create_planet(pos=vector(19.2, 0, 0), radius=0.3, color=color.cyan),
    create_planet(pos=vector(30.06, 0, 0), radius=0.3, color=color.blue),
]

# Create the orbits
orbits = [
    create_orbit(pos=vector(0.39, 0, 0)),
    create_orbit(pos=vector(0.72, 0, 0)),
    create_orbit(pos=vector(1, 0, 0)),
    create_orbit(pos=vector(1.52, 0, 0)),
    create_orbit(pos=vector(5.2, 0, 0)),
    create_orbit(pos=vector(9.54, 0, 0)),
    create_orbit(pos=vector(19.2, 0, 0)),
    create_orbit(pos=vector(30.06, 0, 0)),
]

# Set up the camera
scene.camera.pos = vector(2, 2, 2)
scene.camera.axis = vector(-2, -2, -2)

while True:
    rate(60)


q1 = """Which planet is known as blue planet?
a.earth
b.mumbai
c.chennai
d.bombay"""

q2 = """which one of our is our galaxy?
a.milky way
b.earth
c.mercury
d.venus"""

q3 = """which is the hottest planet in our solar system?
a.earth
b.venus
c.mercury
d.none"""

q4 = """which is the brightest planet?
a.earth
b.venus
c.mercury
d.none"""



questions={q1:"a",q2:"a",q3:"b",q4:"b"}
score=0
name=input("enter your name:")
print("hello",name,"welcome to our mock test")

for i in questions:
    print()
    print(i)
    
    ans=input("enter the answer (a/b/c/d):")
    if ans==questions[i]:
        print("correct answer ,you have scored 1 point")
        score=score+1
        print("current score is :",score)
    else:
        print("wrong answer ,you have lost 1 point")
        score=score-1
        print("current score is :",score)
print("final score is :",score)

