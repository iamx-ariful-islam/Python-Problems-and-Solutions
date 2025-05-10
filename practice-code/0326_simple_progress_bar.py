# pip install alive-progress

import time
from alive_progress import alive_bar


items = range(100)

with alive_bar(len(items)) as bar:
    for item in items:
        time.sleep(0.05)
        bar()