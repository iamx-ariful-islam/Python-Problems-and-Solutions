# pip install rembg
# pip install pillow

from PIL import Image
from rembg import remove


input_path  = 'input_file.jpg'
output_path = 'output_file.png'

input  = Image.open(input_path)
output = remove(input)
output.save(output_path)