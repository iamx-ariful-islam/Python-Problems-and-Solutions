# pip install gofile

import gofile as go


def store_files(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    print('Download Link: ', url['downloadPage'])

store_files('file_name.txt')