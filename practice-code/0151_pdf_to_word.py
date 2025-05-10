# pip install pdf2docx

from typing import Tuple
from pdf2docx import parse, Converter



# method 1
def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input, docx_file=output_file, pages=pages)

    sumary = {'File': input_file, 'Pages': str(pages), 'Output': output_file}


input_file  = 'pdf_file.pdf'
output_file = 'docx_file.docx'

convert_pdf2docx(input_file, output_file)


# method 2
cv = Converter('pdf_file.pdf')
cv.convert('docx_file.docx')
cv.close()