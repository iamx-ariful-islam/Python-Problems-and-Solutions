import os

# set some defult extensions
ext_list = ['.docx','.rpm', '.deb', '.iso']

# get all files from path
def get_files(path):
    for root, _, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] in ext_list:
                print(os.path.join(root, file))

# root
if __name__ == '__main__':
    # set your path to get files
    path = 'D:\\Softwares'
    get_files(path)