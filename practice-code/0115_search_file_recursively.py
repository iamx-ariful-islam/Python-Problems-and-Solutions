# search file recursively

from pathlib import Path

# enter file name
file = Path(input("Enter file name: "))
dirt = Path('/home/work/')


for f in dirt.rglob('*'):
    if f.name.lower() == f.name.lower():
        if f.is_file():
            print(f)