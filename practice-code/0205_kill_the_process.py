# pip install psutil

import psutil


for proc in psutil.process_iter():
    try:
        if proc.pid == 'my_process_id':
            proc.kill()
    except: pass