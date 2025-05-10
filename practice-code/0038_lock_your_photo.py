# pip install cryptography

from cryptography.fernet import Fernet
key_code = Fernet.generate_key()

with open('key.key', 'wb') as fl:
    fl.write(key_code)
    

fernet = Fernet(key=key_code)
with open('<your_photo>.jpg', 'rb') as fl:
    photo_data = fl.read()
    
lock = fernet.encrypt(photo_data)
with open('<your_photo>.jpg', 'wb') as fl:
    fl.write(lock)
    
print('Your photo is locked!')