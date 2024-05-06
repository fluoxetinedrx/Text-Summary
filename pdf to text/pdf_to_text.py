import PyPDF2
import re

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf :
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []
        for page in reader.pages: 
            content = page.extract_text()
            pdf_text.append(content)    
    return pdf_text

# demo
extracted_text = extract_text_from_pdf(r'D:\CNPM\Text-Summary\pdf to text\Lo-trinh-hoc-IELTS-tu-0-8.5.pdf')

doc=''
for text in extracted_text:
    split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
    for message in split_message :
        doc+=message+ ' '

print(doc)
    
    