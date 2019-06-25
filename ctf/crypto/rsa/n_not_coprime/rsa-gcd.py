import gmpy2
import libnum
n = []
c = []
with open("topic.txt") as f:
  for line in f:
    if line.startswith('e = '):
      e = int(line[4:])
    elif line.startswith('n = '):
      x = int(line[4:])
      n.append(x)
    elif line.startswith('c = '):
      x = int(line[4:])
      c.append(x)

def getgcd():
  for i in range(len(n)):
    for j in range(i+1, len(n)):
      p = gmpy2.gcd(n[i], n[j])
      if p > 1 :
        return p, i , j

p,i,j = getgcd()
print p, i, j
q = n[i] / p
phin = (p - 1) * (q - 1)
d = gmpy2.invert(e, phin)
plain = gmpy2.powmod(c[i], d, n[i])
print libnum.n2s(plain)