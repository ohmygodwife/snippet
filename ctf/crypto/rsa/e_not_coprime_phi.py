'''
Writeup:
https://gist.github.com/elliptic-shiho/98bb452dc14e8c40e403
https://github.com/p4-team/ctf/tree/master/2016-03-12-0ctf/rsa
http://www.vuln.cn/6004
Wolframalpha:
https://www.wolframalpha.com/input/?i=x%5E3+%3D+20827907988103030784078915883129+(mod+26440615366395242196516853423447)
'''
#from scryptos import *
import scryptos
import gmpy2
def chinese_remainder(a, n):
      sum = 0
      prod = reduce(lambda a, b: a*b, n)

      for n_i, a_i in zip(n, a):
          p = prod / n_i
          sum += a_i * gmpy2.invert(p, n_i) * p
      return sum % prod

c = 2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524
n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067
e = 3

p1 = 32581479300404876772405716877547
p2 = 27038194053540661979045656526063
p3 = 26440615366395242196516853423447

# from User's Guide to PARI/GP, nth_root function
sqrtnall = 'sqrtnall(x,n)={my(V,r,z,r2);r=sqrtn(x,n,&z);if(!z,error("Impossible case in sqrtn"));if(type(x)=="t_INTMOD"||type(x)=="t_PADIC",r2 = r*z;n=1;while(r2!=r,r2*=z;n++));V=vector(n);V[1]=r;for(i=2,n,V[i]=V[i-1]*z);V}'

c1 = eval(scryptos.parigp([sqrtnall, "Vec(liftall(sqrtnall(Mod(%d, %d), 3)))" % (c, p1)]))
c2 = eval(scryptos.parigp([sqrtnall, "Vec(liftall(sqrtnall(Mod(%d, %d), 3)))" % (c, p2)]))
c3 = eval(scryptos.parigp([sqrtnall, "Vec(liftall(sqrtnall(Mod(%d, %d), 3)))" % (c, p3)]))
print c1, c2, c3

#c1 = [6149264605288583791069539134541, 13404203109409336045283549715377, 13028011585706956936052628027629]
#c2 = [19616973567618515464515107624812]
#c3 = [13374868592866626517389128266735, 7379361747422713811654086477766, 5686385026105901867473638678946]


for x in c1:
  for y in c2:
    for z in c3:
      m = scryptos.crt([x,y,z], [p1,p2,p3]) #chinese_remainder(ak, nk)
      m = hex(m)[2:].rstrip("L")
      if len(m) % 2 != 0:
        m = '0' + m
      d = m.decode("hex")
      if "0ctf" in d:
        print m
        print d
        print d[d.find("0ctf"):].strip()
