import os
import shutil

# enter your path here
path = ''

# find the all files from path
file_name   = os.listdir(path)
# set some default folders name
folder_name = ['Image files', 'Text files', 'CSV files', 'Others']

# create folder if not exists
for x in range(len(folder_name)):
    new_folder_path = os.path.join(path, folder_name[x])
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

# sort the files in file explorer
for file in file_name:
    if ('.png' or '.jpg' or '.jpeg') in file and not os.path.exists(os.path.join(path, 'Image files/' + file)):
        shutil.move(path + file, os.path.join(path, 'Image files/' + file))
    elif '.txt' in file and not os.path.exists(os.path.join(path, 'Text files/' + file)):
        shutil.move(path + file, os.path.join(path, 'Text files/' + file))
    elif '.csv' in file and not os.path.exists(os.path.join(path, 'CSV files/' + file)):
        shutil.move(path + file, os.path.join(path, 'CSV files/' + file))
    else:
        shutil.move(path + file, os.path.join(path, 'Others/' + file))