from flask import Flask, request, jsonify
from summary import Summarizer

app = Flask(__name__, static_folder='ttexxt')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/summary', methods=['POST'])
def summarize():
    if request.method == 'POST':
        data = request.json
        text = data['text']
        summarizer = Summarizer()
        summary, _ = summarizer.summarize(text)
        return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, port=5500, host='127.0.0.1')
