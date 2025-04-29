import pytesseract
from PIL import Image

# Set the path to the Tesseract executable using pytesseract.tesseract_cmd
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"  # Replace with your Tesseract path

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    image_path = "sample.png"  # Replace with the path to your image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:")
    print(extracted_text)
