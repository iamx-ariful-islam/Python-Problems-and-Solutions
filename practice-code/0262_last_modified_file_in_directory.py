# method #1

from pathlib import Path
from datetime import datetime


dpath = Path('/folder/name')
files = {i.name: i.stat().st_mtime for i in dpath.iterdir() if i.is_file()}

print(max(files.items(), key=lambda x: x[1]))



# method #2

from pathlib import Path
from datetime import datetime


dpath = Path('/folder/name')
files = {i.name: i.stat().st_mtime for i in dpath.iterdir() if i.is_file()}

print(sorted(files.items(), key=lambda x: x[1], reverse=True))