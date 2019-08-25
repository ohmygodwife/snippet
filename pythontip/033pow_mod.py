'''https://blog.csdn.net/qq_36760780/article/details/80092665
An = (An-1*Kn) % c
A0 = a^b0  %  c
bn = 0 -> Kn = 1; bn=1 -> Kn = Tn
Tn=( Tn-1 * Tn-1 ) % c
T0= a % c
'''

def pow_mod(a, b, c):
  A = 1
  T = a % c
  while b != 0:
    if b & 1:
      A = A * T % c
    b >>= 1
    T = T * T % c
  return A
  
import time
start = time.clock()
print pow_mod(2,1000000000,20132013)
t1 = time.clock() - start

start = time.clock()
print pow(2,1000000000,20132013)
t2 = time.clock() - start

print t1, t2, t1 > t2


L=['abc','d','efg']
print ' '.join(L)