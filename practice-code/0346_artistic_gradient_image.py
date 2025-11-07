# pip install pillow

from PIL import Image


w = h = 300

img = Image.new('RGB', (w, h))

for x in range(w):
    for y in range(h):
        img.putpixel((x, y), (x % 256, y % 256, (x*y) % 256))

img.show()