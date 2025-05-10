# pip install pypdf2

import getpass
from PyPDF2 import PdfFileWriter, PdfFileReader


# create pdf writer objects
# create pdf reader objects of a pdf file
pdfwriter = PdfFileWriter()
pdfreader = PdfFileReader('fileName.pdf')

for page_num in range(pdfreader.numPages):
    pdfwriter.addPage(pdfreader.getPage(page_num))

# enter password from user
password = getpass.getpass(prompt='Enter password: ')
pdfwriter.encrypt(password)

# write-binary protected pdf file with user input password
with open('protected_fileName.pdf', 'wb') as f:
    pdfwriter.write(f)