# pip install psutil

import os
import psutil

# split the file name and extension
file_name, file_extension = os.path.splitext("/Users/user/abc.txt")

print('File name : ', file_name)
print('Extension : ', file_extension)

# split the file name and extension from a file path
print(os.path.splitext("/Users/user/.bashrc"))
print(os.path.splitext("/Users/user/a.b/image.png"))
print(os.path.splitext("/Users/user/a.b/image_of.png"))
print(os.path.splitext("/Users/user/a.b/image_of.jpg.png.jpg")[1])

sp = os.path.splitext
print(sp("/Users/user/a.b/image.png"))

# find the root paths
def find_root_paths():
    '''Returns a list with all the partitions/mount points which are currently
       mounted on the system.'''
    if os.name == 'nt':
        possible_units = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        units_mounted = []
        for letter in possible_units:
            mountpoint = os.path.normpath(letter + ':/')
            if os.path.exists(mountpoint):
                units_mounted.append(mountpoint)
        root_paths = units_mounted
    else:
        root_paths = ['/']
    return root_paths

print('All root paths list: ', find_root_paths())

# find the all partition list
def PartitionList():
    dkList, fsList = [], []
    disk_parts = psutil.disk_partitions()
    for dp in disk_parts:
        dkList.append(dp.device)
        fsList.append(dp.fstype)
    return (dkList, fsList)

# print the all partition list
dkList = PartitionList()[0]
for x in dkList[::-1]:
    print(x)