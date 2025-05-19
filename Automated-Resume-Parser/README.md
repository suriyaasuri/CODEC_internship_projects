# Automated Resume Parser

## Description
A system to upload, parse, and extract information (name, skills, etc.) from resumes.

## Tech Stack
- Python (spaCy, PDFPlumber)
- Flask
- PostgreSQL

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Download spaCy model:
   ```
   python -m spacy download en_core_web_sm
   ```

3. Run the Flask app:
   ```
   python app/routes.py
   ```

4. Navigate to `http://127.0.0.1:5000` in your browser.

## Output
Extracts candidate details and displays them in a simple web UI.