from flask import Flask, request, jsonify, send_file
from docx import Document
from summarize import Summarize
from return_doc import create
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
def read_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + " "
    return text

def split_words(text, chunk_size=2048):
    words = text.split()
    return ["".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.docx'):
        try:
            content = read_docx(file)
            word_list = split_words(content)
            doc=create(Summarize(word_list))
            return send_file(doc, download_name='summarized_document.docx', as_attachment=True)


        except Exception as e:
            return jsonify({'error': str(e)}), 500

    else:
        return jsonify({'error': 'Invalid file format. Please upload a DOCX file'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
