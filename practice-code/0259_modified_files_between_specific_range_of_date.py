from pathlib import Path
from datetime import datetime


start_day = datetime.strptime('10.02.2025 00', '%d.%m.%Y %H')
end_day   = datetime.strptime('16.02.2025 00', '%d.%m.%Y %H')

files = Path('/folder/name/')
ftime = [(datetime.fromtimestamp(i.stat()[-2]), 1) for i in files.iterdir() if i.is_file()]

for x, y in ftime:
    if start_day < x < end_day:
        print(f'{x:%d.%m.%Y} = {y}')