from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from transformers import pipeline

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load QA model
qa_model = pipeline("question-answering")

@app.route('/')
def home():
    return "Welcome to the QA System API!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    if not data or 'question' not in data or 'file_path' not in data:
        return jsonify({"error": "Invalid request"}), 400

    question = data['question']
    file_path = data['file_path']

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    with open(file_path, 'r') as file:
        document = file.read()

    result = qa_model(question=question, context=document)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
