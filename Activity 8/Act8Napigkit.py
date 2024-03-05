from thinkdsp import SquareSignal

signal = SquareSignal(2200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=500000)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=20, framerate=99000)
wave.apodize()
wave.make_audio()
