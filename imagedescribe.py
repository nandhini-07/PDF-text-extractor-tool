import os
from PIL import Image
from transformers import pipeline, AutoFeatureExtractor

# Initialize the image captioning pipeline
image_caption_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Initialize the feature extractor
feature_extractor = AutoFeatureExtractor.from_pretrained("Salesforce/blip-image-captioning-large")

# Define a function to get image captions
def get_image_caption(image_path):
    try:
        # Open the image from the local file path
        image = Image.open(image_path)

        # Preprocess the image using the feature extractor
        inputs = feature_extractor(images=image, return_tensors="pt")

        # Perform image captioning
        captions = image_caption_pipeline(**inputs)

        # Extract and return the top caption if available
        if captions and isinstance(captions[0], dict) and "caption" in captions[0]:
            top_caption = captions[0]["caption"]
            return top_caption
        else:
            return "No caption found in the image"
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Example usage
if __name__ == "__main__":
    image_path = "peacock.jpeg"

    caption = get_image_caption(image_path)
    print("Image Caption:", caption)
