# search directory recursively

from pathlib import Path


dir_name = input('Enter directory name: ').casefold()

dir_list = Path('/home/user/').rglob('test/*')
only_dir = [x.name for x in dir_list if x.is_dir()]

if dir_name in only_dir:
    print(f'"{dir_name}" Directory exists.')
else:
    print(f'"{dir_name}" Directory does not exists.')