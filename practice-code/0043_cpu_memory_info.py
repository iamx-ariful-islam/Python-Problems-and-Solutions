# pip install psutil

import os
import psutil
import platform

# read the program process info
PID = os.getpid()
PC  = psutil.Process(PID)


# read the side of program
CPU = PC.cpu_percent()/psutil.cpu_count()
mb  = PC.memory_full_info().rss/(1024*1024)
print(f'CPU Usages   \t: {CPU}%')
print(f'Memory Usage \t: {mb}MB')

# read the system info
print('System      \t:', platform.system()+platform.release())
print('Archtecture \t:', platform.architecture()[0]+'/'+platform.machine())

# convert from bytes
def get_size(bytes, suffix="B", factor=1024):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        
TL, UD, FE = 0, 0, 0
for partition in psutil.disk_partitions():
    try: partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError: continue
    TL += partition_usage.total
    UD += partition_usage.used
    FE += partition_usage.free

# read the memory size
print('Memory[T|U|F] \t: '+get_size(psutil.swap_memory().total)+'|'+get_size(psutil.swap_memory().used)+'|'+get_size(psutil.swap_memory().free))
print('Disk[T|U|F]   \t: '+get_size(TL)+'|'+get_size(UD)+'|'+get_size(FE))