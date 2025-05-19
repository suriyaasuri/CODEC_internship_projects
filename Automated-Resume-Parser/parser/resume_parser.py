import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume(file):
    text = ""
    if file.filename.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    else:
        text = file.read().decode('utf-8')

    doc = nlp(text)
    name = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    skills = [token.text for token in doc if token.pos_ == "NOUN"]
    return {"name": name[0] if name else "N/A", "skills": skills[:10]}