import PyPDF2

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

pdf_path = "sample.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
if extracted_text:
    print("Extracted text:")
    print(extracted_text)
else:
    print("No text extracted from the PDF.")
