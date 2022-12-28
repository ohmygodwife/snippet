#private, xiangshang-2022, https://blog.csdn.net/zerorzeror/article/details/127604534
#python3

from binascii import *
import os

path = '1.mp3'
step = 0x139 #sizeof MPEG_FRAME, need to change!!!

f = open(path, 'rb')
size = os.path.getsize(path)

flag = ''
for frame in range(0, size, step):
    f.seek(frame)
    bin_data = bin(int(hexlify(f.read(4)), 16))[2:]
    flag += bin_data[23] #private_bit index: 23

for i in range(0, len(flag), 8):
    flag_r = chr(int(flag[i:i+8], 2))
    print(flag_r,end='')
