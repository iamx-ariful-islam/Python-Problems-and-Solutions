# pip install scipy
# pip install sounddevice

import sounddevice
from scipy.io.wavfile import write


fs = 44100

second = int(input('Enter the recording time in second: '))
print('Recording.....!')

record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels=2)
sounddevice.wait()
write('Myrecording.wav', fs, record_voice)
print('Recording is done. Please check your folder to listen recording')