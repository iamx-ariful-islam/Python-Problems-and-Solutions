# method #1

file = 'file_name.txt'
with open(file) as fopen:
    print(fopen.read())
    
    
# method #2

try:
    file = open('file_name.txt')
    print(file.read())
except IOError:
    print('Error')
finally:
    file.close()
    
    
# method #3

from pathlib import Path

print(Path('file_name.txt').read_text())