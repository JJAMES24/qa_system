from transformers import pipeline
import base64
from io import BytesIO
import os
from docx import Document
import fitz  # PyMuPDF


# Dummy implementation, replace with actual file processing logic
# def process_file(file_path, question):
#     # Implement logic to process the file and return an answer
#     return "Research examples of the documents to create your own version"
qa_pipeline = pipeline("question-answering")

def decode_base64_and_save(base64_data, file_path):
    # Decode base64 data and save it to a file
    file_data = base64.b64decode(base64_data)
    with open(file_path, 'wb') as file:
        file.write(file_data)

def fetch_wikipedia_data(question):
    # Initialize pipeline here (assuming you need it to be a global or
    # to avoid reinitializing it multiple times)
    qa_pipeline = pipeline("question-answering")

    # Dummy implementation for now, replace with actual logic
    context = "Living documents are continually edited and updated."
    result = qa_pipeline(question=question, context=context)
    return result['answer']

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def process_file(file_path, question):
    # Determine file type and process accordingly
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.txt':
        with open(file_path, 'r') as file:
            text = file.read()
    elif file_extension == '.docx':
        text = extract_text_from_docx(file_path)
    elif file_extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    else:
        return "Unsupported file type"

    # Process the text and question using your QA pipeline
    try:
        # Use the QA pipeline to get the answer
        result = qa_pipeline(question=question, context=text)
        answer = result.get('answer', 'No answer found')
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    return answer
    # For demonstration, we return a placeholder
    #return f"Processed text from {file_extension} file."
    
    