# last modification date time of a file

import os
from time import ctime


# set file path with extension
file = "/home/test.txt"

mseconds = os.path.getmtime(file)
print(ctime(mseconds))