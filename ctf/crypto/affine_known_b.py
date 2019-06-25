cipher = 'achjbnpdfherebjsw'
b = 7

flag = []
for ch in cipher:
  x = ord(ch) - ord('a')
  x -= b
  flag.append(x)

print flag
inv = [1,9,21,15,3,19,7,23,11,5,17,25]
for i in inv:
  out = ''
  for j in flag:
    out += chr(j * i % 26 + ord('a'))
  print out
