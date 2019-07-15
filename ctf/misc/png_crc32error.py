'''https://swpuctf.club
'''
import os
import binascii
import struct


misc = open("1.png","rb").read()
target = int(misc[29:33].encode('hex'), 16)

'''width, height
for i in range(65535):
  for j in range(65535):
    data = misc[12:16] + struct.pack('>i',i)+ struct.pack('>i',j) + misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == target:
        print hex(i), hex(j) #0x2d3 0x32f
'''

# heigh ONLY
for j in range(65535):
    data = misc[12:20] + struct.pack('>i',j) + misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == target:
        print hex(j) #0x2d3 0x32f