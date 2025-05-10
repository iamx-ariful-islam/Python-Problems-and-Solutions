# pip install psutil

import psutil


for proc in psutil.process_iter():
    print(f'{proc} = {proc.pid}')