import keras_ocr
from PIL import Image

# Initialize the Keras OCR pipeline
pipeline = keras_ocr.pipeline.Pipeline()

def extract_text_from_image(image_path):
    try:
        # Open the image using Pillow (PIL)
        image = Image.open(image_path)
        
        # Run the OCR pipeline on the image
        prediction_groups = pipeline.recognize([image])
        
        extracted_text = ""
        for predictions in prediction_groups:
            for prediction in predictions:
                text = ' '.join(prediction[0])
                extracted_text += text + " "
        
        return extracted_text.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    image_path = "friend.jpg"  # Replace with the actual image path
    extracted_text = extract_text_from_image(image_path)
    
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("Text extraction failed.")
