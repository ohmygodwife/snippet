'''https://swpuctf.club
'''
import os
import binascii
import struct


misc = open("Easy.png","rb").read()

for i in range(1024):
  for j in range(1024):
    data = misc[12:16] + struct.pack('>i',i)+ struct.pack('>i',j) + misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0x9fb1cbb0:
        print hex(i), hex(j) #0x2d3 0x32f