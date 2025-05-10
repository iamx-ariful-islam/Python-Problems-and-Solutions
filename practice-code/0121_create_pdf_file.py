# pip install reportlab

from reportlab.pdfgen import canvas

pdf_file = canvas.Canvas('example1.pdf')

pdf_file.drawString(72, 720, "Hello World!")
pdf_file.drawString(72, 700, "Free PDF Documents")
pdf_file.drawString(72, 680, "This is the Reportlab")

pdf_file.save()