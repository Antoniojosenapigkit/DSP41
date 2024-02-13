import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100  
frequency = 440 
duration = 2

t = np.arange(int(sample_rate * duration)) / sample_rate

signal = 0.5 * np.sin(2 * np.pi * frequency * t)

signal = (signal / np.max(np.abs(signal))) * 32767

signal = signal.astype(np.int16)

write('soundwave.wav', sample_rate, signal)

from IPython.display import Audio
Audio(signal, rate=sample_rate)
