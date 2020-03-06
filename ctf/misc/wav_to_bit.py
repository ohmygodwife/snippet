'''Unpleasant_music, wdb3rd-2018, http://since1994.cn/?p=198
'''
import wave
import libnum
import numpy as np

def wav_to_bit(file):
  wavfile = wave.open(file, 'rb')
  params = wavfile.getparams() #Returns a namedtuple() (nchannels, sampwidth, framerate, nframes, comptype, compname),(1, 2, 8000, 159999, 'NONE', 'not compressed')
  print params
  framesra,frameswav= params[2],params[3]
  nframes = wavfile.getnframes()
  str_data = wavfile.readframes(nframes)
  wave_data = np.fromstring(str_data, dtype=np.short)

  bit = ''
  for i in range(1, len(wave_data) - 1):
    if wave_data[i-1] < wave_data[i] and wave_data[i] > wave_data[i+1]: #ONLY handle peak
      if wave_data[i] > 24000: ##16381 32665 16220 32086 ...
        bit += '1'
      else:
        bit += '0'
  return bit

bit = wav_to_bit('music.wav')
with open('out.rar', 'wb') as f:
  f.write(libnum.b2s(bit))

