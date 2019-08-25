'''(a*b) % c = (a%c * b%c) % c
'''
a = 10
b = 3
x = 999999998
y = 999999999

a = a * pow(10, x - 1, b) % b
ret = ''
for i in range(y - x + 1):
  a *= 10
  ret += str(a/b)
  a %= b
  
print ret