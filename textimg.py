import easyocr
from PIL import Image

def extract_text_from_image(image_path, languages=['en']):
    try:
        # Load the EasyOCR reader with specified languages
        reader = easyocr.Reader(languages)
        
        # Load the image
        image = Image.open(image_path)
        
        # Perform OCR on the image
        results = reader.readtext(image)
        
        # Close the image
        image.close()
        
        # Print the extracted text and bounding box information
        for (text, bounding_box, prob) in results:
            print(f"Text: {text}")
            print(f"Bounding Box: {bounding_box}")
            print(f"Confidence: {prob}")
            print("--------")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = 'sample.png'  # Replace with your image path
    extract_text_from_image(image_path)
