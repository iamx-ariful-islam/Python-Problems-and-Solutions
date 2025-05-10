import os
import sys
import time
import itertools
import threading


work = False; n = 0

def animate_str():
    _str = ''
    for n in 'Starting your console application....':
        sys.stdout.flush()
        sys.stdout.write('\r' + _str + ' ' + n)
        _str += n
        time.sleep(.10)
    sys.stdout.flush()
    sys.stdout.write('\r' + _str)
    
def read_str():
    _str = "Starting your console application...."
    global n
    if n == len(_str): n = 0
    load_str = _str[:n] + _str[n].upper() + _str[n + 1:]
    n += 1
    return load_str
    
def loading_animate():
    for ch in itertools.cycle(['|', '/', '-', '\\']):
        if work: break
        sys.stdout.write('\r' + read_str() + ch)
        sys.stdout.flush()
        time.sleep(0.15)

animate_str()
th = threading.Thread(target = loading_animate)
th.start()
    


def input_banner():
    st = 'hi, this is me!'
    time.sleep(10)
    return st

def print_banner(s):
    print(s)
    print('How are your')

_str = input_banner()

work = True
os.system('cls' if os.name == 'nt' else 'clear')

print_banner(_str)


'''output:

Starting your console Application..../
'''