import docx

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    input_file_path = "solarsystem.docx"  # Replace with the actual path of your Word document
    extracted_text = extract_text_from_docx(input_file_path)
    
    if extracted_text:
        print("Extracted text:")
        print(extracted_text)
    else:
        print("Failed to extract text from the document.")
