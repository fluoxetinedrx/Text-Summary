import docx

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

docx_file = r'D:\CNPM\Text-Summary\word to text\test.docx'
text = extract_text_from_docx(docx_file)
print(text)