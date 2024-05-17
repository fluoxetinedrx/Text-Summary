from flask import Flask, request, jsonify
from summary import Summarizer
from werkzeug.utils import secure_filename
import os
import mimetypes
from text_processing import preprocess_text, extract_text_from_docx, extract_text_from_pdf

app = Flask(__name__, static_folder='frontend')

# Thư mục lưu trữ tạm thời các tệp được tải lên
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Đảm bảo thư mục tồn tại
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/summary', methods=['POST'])
def summarize():
    data = request.json
    text = data['text']
    text = preprocess_text(text)  # Xử lý văn bản trước khi tóm tắt
    summarizer = Summarizer()
    summary, _ = summarizer.summarize(text)
    return jsonify({'summary': summary})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Kiểm tra định dạng của tệp và trích xuất văn bản tương ứng
        mime_type, _ = mimetypes.guess_type(filepath)
        if mime_type == 'application/pdf':
            text = extract_text_from_pdf(filepath)
        elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            text = extract_text_from_docx(filepath)
        else:
            os.remove(filepath)
            return jsonify({'error': 'Unsupported file type'})
        
        text = preprocess_text(text)
        
        # Xóa tệp sau khi xử lý để giải phóng dung lượng
        os.remove(filepath)
        
        # Trả về văn bản từ tệp đã xử lý
        return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True, port=5500, host='127.0.0.1')
