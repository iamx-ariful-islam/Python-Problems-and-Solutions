import os


PATH = 'C:\\working\\folder'

file_count = 0
dir_count  = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:', root)
    for _ in dirs: dir_count += 1
    for _ in files: file_count += 1
    

print('Number of files:', file_count)
print('Number of directories:', dir_count)
print('Total:', file_count + dir_count)