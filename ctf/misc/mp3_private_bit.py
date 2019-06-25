'''http://www.liquor994.cn/index.php/archives/159/
'''
flag = ''
with open('Jingle Bells.csv', 'r') as f:
  offset = len('private_bit : 1,')
  for line in f:
    start = line.find('private_bit : 1,')
    if start >= 0:
      start += offset
      flag += line[start: start + 1]
print flag

'''
#match with 'ff fb 9*', not safe, because it could occurs in frame data
data=open('Jingle Bells.mp3', 'rb').read()
array = [ord(i) for i in data]

flag = ''
for i in range(0x1199d, len(array) - 2): #010editor tell first frame in 0x1199d
  if (array[i] == 0xff and array[i+1] == 0xfb and array[i+2]/16==9):
    #print hex(i), array[i+2]%2
    flag +=str(array[i+2]%2)


print flag
'''

import libnum
print libnum.b2s(flag)
