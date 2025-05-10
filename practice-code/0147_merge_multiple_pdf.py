# pip install pypdf2

import os
from PyPDF2 import PdfFileMerger


original_file = 'filename.pdf'

merger = PdfFileMerger()
# find and append all pdf file in root directory
for items in os.listdir():
    if items.endswith('*.pdf'):
        merger.append(items)

merger.write('final_pdf.pdf')

merger = PdfFileMerger()
# read original file into binary mode
with open(original_file, 'rb') as fin:
    merger.append(PdfFileMerger(fin))

# remove original file
os.remove(original_file)
merger.close()