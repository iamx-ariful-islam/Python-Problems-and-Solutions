# pip install zipfile

from zipfile import ZipFile


with ZipFile('<your_zip_file>.zip', 'r') as zip_object:
    zip_object.extractall()

print(zip_object.namelist())