M = 15424654874903
A = 16546484
B = 4548674875
P = (6478678675, 5636379357093)
k = 546768
E = EllipticCurve(GF(M),[A,B]) #GF is short for FiniteField
P = E.point(P)

Q = k*P
print(P)
print(Q)

'''
#https://xz.aliyun.com/t/6910, wrong answer after n=1776, use sage instead!!!
a=16546484
p=15424654874903
def egcd(t, b):
    if t == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % t, t)
      return (g, x - (b // t) * y, y)

def modinv(o, m):
    g, x, y = egcd(o, m)
    if g != 1:
      raise Exception('modular inverse does not exist')
    else:
      return x % m

def ecc_m(x1,y1,x2,y2):
    if ((x1 == x2) & (y1 == y2)):
        fenzi=3*x1*x1+a
        fenmu=2*y1
    else:
        fenzi = y2 - y1
        fenmu = x2 - x1
    m=(abs(fenzi) * modinv(abs(fenmu), p)) % p
    if ((fenzi >= 0 & fenmu >= 0) | (fenzi < 0 & fenmu < 0)):
        return m
    else:
        return p - m

def ecc_x(x1,x2,m):
    result_x = m*m-x1-x2
    if result_x>0:
        return result_x%p
    else:
        p1=p
        if abs(result_x)>p1:
            shang=abs(result_x)/p
            p1=shang*p+p
        return p1+result_x

def ecc_y(x1,result_x,y1,m):
    result_y = m*(x1-result_x)-y1
    if result_y>0:
        return result_y%p
    else:
        p1 = p
        if abs(result_y) > p1:
            shang = abs(result_y) / p
            p1 = shang * p + p
        return p1 + result_y

def ecc_result_x(x1,y1,x2,y2):
    m = ecc_m(x1,y1,x2,y2)
    result_x=ecc_x(x1,x2,m)
    return result_x

def ecc_result_y(x1,y1,x2,y2):
    m = ecc_m(x1,y1,x2,y2)
    result_x = ecc_x(x1, x2, m)
    result_y=ecc_y(x1, result_x, y1, m)
    return result_y

x1=x2=x3=6478678675
y1=y2=5636379357093
n=1776
while(n>0):
    x2=ecc_result_x(x1,y1,x2,y2)
    y2=ecc_result_y(x1,y1,x3,y2)
    x3=x2
    n-=1
print x2,y2
result = x2+y2
flag = "XUSTCTF{%s}"%result
print(flag)
'''