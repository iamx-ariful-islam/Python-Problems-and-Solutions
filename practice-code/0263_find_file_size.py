import bisect
from pathlib import Path


# size = [1, 1e+3, 1e+6, 1e+9]
size  = [1, 2**10, 2**20, 2**30]
unit  = ['B', 'K', 'M', 'G']
fpath = input('Enter file name: ')
fsize = Path(fpath).stat().st_size

def convert(bytes):
    if bytes != 0:
        index = bisect.bisect(size, bytes) - 1
        return f'{bytes/size[index]:.1f}{unit[index]}'
    else:
        return '0B'
    
print(f'{convert(fsize)} {fpath}')