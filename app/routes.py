import os
from flask import Blueprint, request, jsonify,render_template
from werkzeug.utils import secure_filename
from utils import process_file, fetch_wikipedia_data
import logging
import base64
import os
from io import BytesIO

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/ask', methods=['POST'])
def ask():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415

    try:
        data = request.get_json()
        question = data.get('question')
        file_data = data.get('file')

        if not question or not file_data:
            return jsonify({'error': 'Invalid request'}), 400

        filename = secure_filename(file_data.get('filename'))
        file_content = file_data.get('content')

        # Decode the base64 content
        if isinstance(file_content, str):
            file_content = base64.b64decode(file_content)

        # Save the file to the server
        file_path = os.path.join('uploads', filename)
        with open(file_path, 'wb') as f:
            f.write(file_content)

        # Process the file
        document_answer = process_file(file_path, question)
        wikipedia_answer = fetch_wikipedia_data(question)

        # Clean up the file after processing
        os.remove(file_path)

        return jsonify({
            'document_answer': document_answer,
            'wikipedia_answer': wikipedia_answer
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
