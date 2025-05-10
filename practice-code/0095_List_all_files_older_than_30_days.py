import os
import glob
from datetime import datetime


today = datetime.today()
print('Below files are older than 30 days')
for i in glob.glob('/file/path/*'): # Enter file path
    mtime = datetime.fromtimestamp(os.stat(i)[0])
    filetime = mtime - today
    if filetime.days <= -30:
        print(f'{os.path.basename(i):<20} older {abs(filetime.days)} days')