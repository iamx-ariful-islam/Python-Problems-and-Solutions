# pip install fitz

import fitz


def extract_text(pdf_path):
    doc  = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text


pdf_path = 'pdf_file_name.pdf'
text = extract_text(pdf_path)
print(text)