import PyPDF2

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file,'rb') as pdf:
        reader=PyPDF2.PdfFileReader(pdf, strict=False)
        pdf_text=[]

        for pages in reader.pages:
            content= page.extract_text()
            pdf_text.append(content)

        return pdf_text

if __name__== '__main__':
    extracted_text=extract_text_from_pdf('sample.pdf')
    for text in extracted_text:
        print(text)
        

