# pip install fitz

import os
import fitz


def extract_images(pdf_path, output_dir):
    doc  = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image['image']
            image_ext = base_image('ext')
            image_filename = os.path.join(output_dir, f'image_{page+1}_{xref}.{image_ext}')
            with open(image_filename, 'wb') as image_file:
                image_file.write(image_bytes)


pdf_path = 'pdf_file_name.pdf'
output_dir = 'images'
os.makedirs(output_dir, exist_ok=True)
extract_images(pdf_path, output_dir)