# pip install pdf2docx

from pdf2docx import Converter


pdf_file  = 'file_name.pdf'
docx_file = 'file_name.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()