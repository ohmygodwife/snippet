#https://huangx607087.online/2021/03/25/ECCNotes3
#Sagemath
c=[]
a=[]
b=[]
n=[]
Fzlist=[]
Fmlist=[]
Dlist=[]
for i in range(70):
    R.<x>=PolynomialRing(Zmod(n[i]))
    Fz=x*(3*x^4+6*a[i]*x^2+12*b[i]*x-a[i]^2)^2-8*(x^3+a[i]*x+b[i])*(x^6+5*a[i]*x^4+20*b[i]*x^3-5*a[i]^2*x^2-4*a[i]*b[i]*x-8*b[i]^2-a[i]^3)
    Fm=(3*x^4+6*a[i]*x^2+12*b[i]*x-a[i]^2)^2
    Fzlist.append(Fz)
    Fmlist.append(Fm*c[i])
    Dlist.append(Fz-c[i]*Fm)
Crtlist=[[0 for _ in range(70)] for __ in range(10)]
for i in range(70):
    for j in range(10):
        Crtlist[j][i]=ZZ(Dlist[i][j])
A=[]
for i in range(10):
    A.append(CRT(Crtlist[i],n))
N=1
for i in n:
    N*=i
O.<y>=PolynomialRing(Zmod(N))
S=0
for i in range(10):
    S+=A[i]*y^i
print('Finding Roots')
oo,oooo,ooooo=1,2,3
S.small_roots(epsilon=1/16)
[3088969433059681806521206959873975785377227976800172674306727155831805513908352148702210247662586117242206183337522557]