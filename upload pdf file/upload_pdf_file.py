from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(filename)
            text = extract_text_from_pdf(filename)
            os.remove(filename)
            return text

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
