# pip install moviepy

from moviepy import VideoFileClip


videoClip = VideoFileClip('<your_file>.mp4')
videoClip.write_gif('<your_file>.gif')