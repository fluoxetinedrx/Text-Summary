import re
from docx import Document
import fitz
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_file: str) -> str:
    """
    Extract text from a PDF file.
    """
    with fitz.open(pdf_file) as pdf:
        pdf_text = ""
        for page in pdf:
            pdf_text += page.get_text()
            
            # Xử lý hình ảnh nếu có
            for img in page.get_images(full=True):
                xref = img[0]
                base_image = pdf.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                
                # Sử dụng Tesseract để trích xuất văn bản từ hình ảnh
                pdf_text += pytesseract.image_to_string(image, lang='vie')
                
    return pdf_text

def extract_text_from_docx(docx_file: str) -> str:
    """
    Extract text from a .docx file.
    """
    doc = Document(docx_file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
        
    # Xử lý hình ảnh nếu có
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image = rel.target_part.blob
            image = Image.open(io.BytesIO(image))
            full_text.append(pytesseract.image_to_string(image, lang='vie'))
            
    return '\n'.join(full_text)

def preprocess_text(text: str) -> str:
    # Bách xử lý văn bản cho sạch đẹp vào hàm này
    return text
