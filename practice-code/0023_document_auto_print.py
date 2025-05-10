# pip install pywin32
# pip install win32print

import os
import win32api
import win32print


# auto print document
def print_doc(flName):
    DPrinter = win32print.GetDefaultPrinter()
    try:
        try: win32api.ShellExecute(0, "printto", flName, '"%s"' % DPrinter, ".", 0)
        except: win32api.ShellExecute (0, "print", flName, '/d:"%s"' % DPrinter, ".", 0)
    except:
        try: os.startfile(flName, 'print')
        except: print('Printable device not work!')

# root
if __name__ == '__main__':
    # enter your file name to print
    flName = input('Enter file name: ')
    print('Your file : ', flName)
    print_doc(flName)