import os

if not os.path.exists('thinkdsp.py'):
    !wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py

from thinkdsp import TriangleSignal
from thinkdsp import decorate

signal = TriangleSignal(600)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=5000)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=5, framerate=5000)
wave.apodize()
wave.make_audio()
