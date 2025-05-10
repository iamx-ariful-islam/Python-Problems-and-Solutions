# pip install alive-progress

import time
from alive_progress import alive_bar


tasks = ['task1', 'task2', 'task3', 'task4']

with alive_bar(len(tasks), title='Processing Tasks') as bar:
    for task in tasks:
        time.sleep(0.5)
        bar.text = f'Working on {task}'
        bar()