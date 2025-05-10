# pip install pypdf2
# pip install pyttsx3

import PyPDF2
import pyttsx3


path = open('pdf_file.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(path)

speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()

speak.stop()