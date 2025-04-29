from PIL import Image, ImageDraw, ImageFont

def generate_image_with_text(text, output_file):
    # Create a blank image
    image = Image.new("RGB", (800, 600), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Add text to the image
    font = ImageFont.truetype("arial.ttf", size=40)
    draw.text((100, 100), text, fill="black", font=font)

    # Save the image
    image.save(output_file)

# Example usage:
text = "Hello, this is a test."
generate_image_with_text(text, "output_image.png")
