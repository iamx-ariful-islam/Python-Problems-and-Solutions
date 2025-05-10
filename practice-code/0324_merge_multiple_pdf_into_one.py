# pip install fitz

import fitz


def merge_pdfs (pdf_list, output_pdf):
    merged_doc = fitz.open()
    for pdf in pdf_list:
        with fitz.open(pdf) as doc:
            merged_doc.insert_pdf (doc)
    merged_doc.save(output_pdf)


pdf_list = ["file_name1.pdf", "file_name2.pdf"]
output_pdf = "marge_pdfs.pdf"
merge_pdfs(pdf_list, output_pdf)