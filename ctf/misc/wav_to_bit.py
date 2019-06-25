import wave
import time
import numpy as np

WAVE = wave.open('music.wav', 'rb')

nframes = WAVE.getnframes()

str_data = WAVE.readframes(nframes)
wave_data = np.fromstring(str_data, dtype=np.short)

for frame in wave_data:
  #frame = int(frame)
  print frame