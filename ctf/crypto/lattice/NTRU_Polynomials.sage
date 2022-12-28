#dasctf-202103
#http://www.zbc53.top/archives/63/

def check(List):
    flag=True
    for i in List:
        if abs(i)>1:
            flag=False
            break
    return flag
 
def balancedmod(f,N,q):
    g = list(((f[i] + q//2) %q) - q//2 for i in range(N))
    return Zx(g)
 
def convolution(f,g,N):
    return (f*g) % (x^N-1)
 
def invertmodprime(f,N,p):
    T = Zx.change_ring(Integers(p)).quotient(x^N-1)
    return Zx(lift(1 / T(f)))
 
def decrypt(ciphertext,secretkey,N,q,p):
    f,fp = secretkey
    a = balancedmod(convolution(ciphertext,f,N),N,q)
    return balancedmod(convolution(a,fp,N),N,p)
 
Zx.<x>=ZZ[]
hx=14443*x^52 + 10616*x^51 + 11177*x^50 + 24769*x^49 + 23510*x^48 + 23059*x^47 + 21848*x^46 + 24145*x^45 + 12420*x^44 + 1976*x^43 + 16947*x^42 + 7373*x^41 + 16708*x^40 + 18435*x^39 + 18561*x^38 + 21557*x^37 + 16115*x^36 + 7873*x^35 + 20005*x^34 + 11543*x^33 + 9488*x^32 + 2865*x^31 + 11797*x^30 + 2961*x^29 + 14944*x^28 + 22631*x^27 + 24061*x^26 + 9792*x^25 + 6791*x^24 + 10423*x^23 + 3534*x^22 + 26233*x^21 + 14223*x^20 + 15555*x^19 + 3381*x^18 + 23641*x^17 + 2697*x^16 + 11303*x^15 + 6030*x^14 + 7355*x^13 + 20693*x^12 + 1768*x^11 + 10059*x^10 + 27822*x^9 + 8150*x^8 + 5458*x^7 + 21270*x^6 + 22651*x^5 + 8381*x^4 + 2819*x^3 + 3987*x^2 + 8610*x + 6022
 
flag=hx.list()
 
N = 53
q = 28019
p = 257
M=matrix([[0 for _ in range(2*N)] for _ in range(2*N)])
for i in range(N):
    for j in range(N):
        M[i+N,j] = int(flag[j-i])
        if i == j:
            M[i,j] = q
            M[N+i,N+j] =  1
 
ex=7367*x^52 + 24215*x^51 + 5438*x^50 + 7552*x^49 + 22666*x^48 + 21907*x^47 + 10572*x^46 + 19756*x^45 + 4083*x^44 + 22080*x^43 + 1757*x^42 + 5708*x^41 + 22838*x^40 + 4022*x^39 + 9239*x^38 + 1949*x^37 + 27073*x^36 + 8192*x^35 + 955*x^34 + 4373*x^33 + 17877*x^32 + 25592*x^31 + 13535*x^30 + 185*x^29 + 9471*x^28 + 9793*x^27 + 22637*x^26 + 3293*x^25 + 27047*x^24 + 21985*x^23 + 13584*x^22 + 6809*x^21 + 24770*x^20 + 16964*x^19 + 8866*x^18 + 22102*x^17 + 18006*x^16 + 3198*x^15 + 19024*x^14 + 2777*x^13 + 9252*x^12 + 9684*x^11 + 3604*x^10 + 7840*x^9 + 17573*x^8 + 11382*x^7 + 12726*x^6 + 6811*x^5 + 10104*x^4 + 7485*x^3 + 858*x^2 + 15100*x + 15860
 
for i in M.LLL():
    if check(i):
        fx=Zx(list(i[N:]))
        flag=""
        try:
            fp = invertmodprime(fx,N,p)
            for j in decrypt(ex,(fx,fp),N,q,p).list():
                flag+=chr(abs(j))
            if "DASCTF" in flag:
                print(flag)
                break
        except:
            pass
        #DASCTF{9bba98e8024da44a3250acbc06bebc7b}
