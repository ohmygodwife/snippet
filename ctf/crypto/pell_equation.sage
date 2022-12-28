#x**2 - d*y**2 = 1, https://zhuanlan.zhihu.com/p/365860557

def basic_solution(d):
  frac = continued_fraction(sqrt(d))
  i = 1
  while True:
    x = frac.numerator(i)
    y = frac.denominator(i)
    if x**2 - d*y**2 == -1:
      return (x, y)
    i += 1
    
def generic_solution(x0, d, y0):
  m0 = matrix([[x0,d*y0], [y0, x0]])
  x0y0 = matrix([[x0], [y0]])
  m = m0
  while True:
    z = m*x0y0
    yield z[0][0], z[1][0]
    m = m*m0
    
d=39352
(x0, y0) = basic_solution(d)
print(x0, y0, x0**2-d*y0**2)

for x,y in generic_solution(x0, d, y0):
  print(x,y, x**2-d*y**2)
  raw_input()