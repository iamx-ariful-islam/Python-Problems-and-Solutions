# pip install psutil

import psutil


# found partition list with file system
def partition_list():
    info = {}
    disk_parts = psutil.disk_partitions()
    for dp in disk_parts:
        info[dp.device] =  dp.fstype
    return info

# root
if __name__ == '__main__':
    print('Partitions:', partition_list())


'''output:

Partitions: {'C:\\': 'NTFS', 'D:\\': 'NTFS', 'E:\\': 'NTFS'}
'''