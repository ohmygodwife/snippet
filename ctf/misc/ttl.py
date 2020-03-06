import libnum

flag = ''
with open('t.txt', 'rb') as f:
  for line in f:
    v = int(line)
    flag += '{:08b}'.format(v)[0:2]
    
flag = libnum.b2s(flag).decode('hex')

with open('out.zip', 'wb') as f:
  f.write(flag)