# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# generate a square wave
t = np.linspace(0, 1, 500, endpoint=False)
square_wave = np.where(np.sin(2*np.pi*t) >= 0, 1, -1)

# compute fft
fft_data = np.fft.fft(square_wave)

# get frequency axis
freq_axis = np.fft.fftfreq(len(square_wave), t[1] - t[0])

# plot square wave and fft magnitude
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, square_wave)
axs[0].set_xlabel('Time(s)')
axs[0].set_ylabel('Amplitude')
axs[1].plot(freq_axis, np.abs(fft_data))
axs[1].set_xlim([0, 10])
axs[1].set_xlabel('Frequency(Hz)')
axs[1].set_ylabel('Magnitude')
plt.show()