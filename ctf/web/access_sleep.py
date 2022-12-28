#hfctf-2021
import re

array = []
with open('access.log') as f:
    for line in f:
        m = re.search("\:(\d+) \+0000\] \"GET \/index\.php\?id=1\'%20and%20if\(ord\(substr\(\(select%20flag%20from%20flllag\),(\d+),1\)\)=(\d+),sleep", line)
        if m:
            array.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

flag = ['\0'] * 35
for i in range(len(array) - 1):
    a = array[i+1][0]
    if a < array[i][0]:
        a += 60
    if a - array[i][0] >= 2:
        flag[array[i][1]] = chr(array[i][2])
        
print ''.join(flag)
print 'ZmxhZ3tZb3VfYXJlX3NvX2dyZWF0fQ=='.decode('base64')

'''


f = open ('access.log')
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
'''