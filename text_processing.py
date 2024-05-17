import re
from docx import Document
import fitz

def extract_text_from_pdf(pdf_file: str) -> str:
    """
    Extract text from a PDF file.
    """
    with fitz.open(pdf_file) as pdf:
        pdf_text = ""
        for page in pdf:
            pdf_text += page.get_text()
    return pdf_text

def extract_text_from_docx(docx_file: str) -> str:
    """
    Extract text from a .docx file.
    """
    doc = Document(docx_file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def preprocess_text(text: str) -> str:
    # Bách xử lý văn bản cho sạch đẹp vào hàm này
    return text
