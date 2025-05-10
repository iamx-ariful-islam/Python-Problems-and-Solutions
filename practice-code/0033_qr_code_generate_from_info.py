# pip install PyQRCode
# pip install Pillow

import pyqrcode
from PIL import Image


# generate qr code with png format
def generate_qrcode(info):
    qr_code = pyqrcode.create(info)
    qr_code.png('info_qr.png', scale=5)
    Image.open('info_qr.png')

# root
if __name__ == '__main__':
    info = input('Enter anything to generate QR: ')
    generate_qrcode(info)