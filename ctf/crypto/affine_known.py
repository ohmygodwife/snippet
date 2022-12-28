#enc: y = a*x+b mod n, dec: x = invert(a, n) * (y-b) mod n, n normally to be 26

import gmpy2

def inv_array(n):
  array = []
  for i in range(n):
    if gmpy2.gcd(i, n) == 1:
      array.append(gmpy2.invert(i, n))
  return array

#fangshe, anheng-181124, https://www.anquanke.com/post/id/166492
def known_b_n():
  cipher = 'achjbnpdfherebjsw'
  b = 7
  n = 26

  arr = []
  for ch in cipher:
    x = ord(ch) - ord('a')
    x -= b
    arr.append(x)

  print arr
  inv = inv_array(n)
  for i in inv:
    out = ''
    for j in arr:
      out += chr(j * i % 26 + ord('a'))
    print out

#known_b_n()

def guess_n(a, b, m, c):
  for n in range(2, a):
    if gmpy2.gcd(n, a) == 1:
      match = True
      for j in range(len(m)):
        x = ord(m[j]) - ord('a')
        y = ord(c[j]) - ord('a')
        if (a * x + b) % n != y % n:
          match = False
          break
      if match:
        return n 

#fangshe, wdb-2020-3rd, https://y-y-k.tk/2020/05/18
#a, b also specified as k1, k2
def known_a_b():
  a = 123456
  b = 321564
  
  m = 'flag'
  c = 'kgws{m8u8cm65-ue9k-44k5-8361-we225m76eeww}'
  
  n = guess_n(a, b, m, c)
  inv = gmpy2.invert(a, n)
  flag = ''
  for i in c:
    y = ord(i)
    if y >= ord('a') and y <= ord('z'):
      x = (inv * (y - ord('a') - b)) % n + ord('a')
      flag += chr(x)
    else:
      flag += i
  print flag
  
known_a_b()