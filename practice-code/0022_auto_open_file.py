import os
import platform


# find system and open file
def open_file(flName):
    if os.path.exists(flName):
        if sys == 'Windows': os.startfile(flName)
        elif sys == 'Darwin': os.system('open', flName)
        elif sys == 'Linux' or 'Java': os.system('xdg-open', flName)
        else: print('Not defined!')
    else: print('File not found')

# root
if __name__ == '__main__':
    sys = platform.system()
    # enter your file name to view
    flName = input('Enter file name: ')
    print('Your file : ', flName)
    open_file(flName)