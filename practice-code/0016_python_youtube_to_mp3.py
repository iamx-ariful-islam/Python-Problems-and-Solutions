# pip install pytube

import os
from pytube import YouTube

# enter youtube url
yurl = input('Enter url : ')

yt = YouTube(yurl)

video = yt.streams.filter(abr='128kbps').last()

output_file = video.download()

# find the base file name and it's extension
base_file, ext = os.path.splitext(output_file)

# create the new file name with .mp3 extension
new_file = base_file + '.mp3'

# change the output file name by new file name
os.rename(output_file, new_file)

print('Download was successful.\nFile : ', new_file)