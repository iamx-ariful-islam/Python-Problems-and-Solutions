import os

PATH = 'D:'

fileCount = 0
dirCount  = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:', root)
    for _ in dirs:
        dirCount += 1
    for _ in files:
        fileCount += 1

print('Number of files:', fileCount)
print('Number of directories:', dirCount)
print('Total:', (dirCount + fileCount))