# QA System API

This is a simple Question-Answering System API using Flask and Hugging Face Transformers.

## Youtube Video

Please find the link to youtube presentation here : https://youtu.be/Pw_dP39b0XQ

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JJAMES24/qa_system.git
   cd qa_system
   ```

2. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python3 app/main.py
   ```

## Endpoints

### Upload Document

- **URL:** `/upload`
- **Method:** `POST`
- **Form Data:**
  - `file`: The document file to upload.
- **Response:**
  - `200 OK` on success with a JSON containing the file path.
  - `400 Bad Request` if no file is provided or if the file is empty.

### Ask Question

- **URL:** `/ask`
- **Method:** `POST`
- **JSON Body:**
  - `question`: The question to ask.
  - `file_path`: The path to the uploaded document.
- **Response:**
  - `200 OK` with a JSON containing the answer.
  - `400 Bad Request` if the request is invalid.
  - `404 Not Found` if the file is not found.

## Example Usage

### Upload Document

```bash
curl -F "file=@/path/to/your/document.txt" http://127.0.0.1:5000/upload
