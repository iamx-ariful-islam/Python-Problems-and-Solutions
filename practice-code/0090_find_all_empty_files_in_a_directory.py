from pathlib import Path


# set your directory path
dpath = Path('/home/me/work')

# find the empty files
files = [i for i in dpath.iterdir() if i.is_file()]

# print the empty files
for file in files:
    if not file.read_text():
        print(file)