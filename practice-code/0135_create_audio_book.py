# pip install gtts

import os
from gtts import gTTS


def create_audio_book(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as fl:
        text = fl.read()
    
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    
    print(f'Audio book saved as {output_file}')
    

text_file   = 'hello_text.txt'
output_file = 'audio_book.mp3'

create_audio_book(text_file, output_file)
os.system(f"start {output_file}")