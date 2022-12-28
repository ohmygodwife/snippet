#cmcc\180816\reversebin
import re

f = open ('accessx.log')
list = f.readlines()

flag = ''
j = 0
byte = 0
for i in range(len(list) - 1):
  t1 = re.search("01/Mar/2015:13:\d{2}:(\d{2})", list[i]).group(1)
  t2 = re.search("01/Mar/2015:13:\d{2}:(\d{2})", list[i+1]).group(1)
  if cmp(t1, t2) != 0:
    byte += 2**j
  j += 1
  if j == 7:
    print bin(byte)
    flag += chr(byte)
    byte = 0
    j = 0

#final byte:
print bin(byte)
flag += chr(byte)
print flag