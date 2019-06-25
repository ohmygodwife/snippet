# -*- coding: utf-8 -*-
'''https://www.jianshu.com/p/128b203dfdd8
'''


# 密文
Cs = r"Pu yfo of oin hvy ufa hrpkpyb, jlar ph hopkk py oin hvy oinan, svo jnjpkk klvbi rfan zfyupgnyo zlkr; pu ovayng of ufvyg iph fjy hilgfj, lmmafmaplon nhzlmn, oin hvy jpkk sn oiafvbi oin inlao,jlar nlzi mklzn snipyg oin zfayna; pu ly fvohoanozing mlkr zlyyfo ulkk svoonaukx, oiny zknyzing jlcpyb larh, bpcny mfjna; pu P zly'o ilcn sapbio hrpkn, po jpkk ulzn of oin hvyhipyn, lyg hvyhipyn hrpkn ofbnoina, py uvkk skffr."

charTable = [ chr(c) for c in range(97,123)]
frequencyTable = [4, 19, 14, 0, 13, 8, 17, 18, 7, 3, 11, 2, 20, 12, 15, 24, 22, 6, 1, 21, 10, 23, 9, 16, 25]

# 删除预留的标点
def del_point(c):
    if c in [' ', ',', '.', ';', '\'', '?', '!']:
        return False
    return True

def get_int_by_char(c):
    return charTable.index(c)

def get_char_by_int(i):
    return charTable[i]    

# 最大公约数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

# 排序
def sort_by_value(d):
    items = d.items()
    backitems = [ [v[1],v[0]] for v in items ]
    backitems = sorted(backitems, reverse = True)
    return [ backitems[i][1] for i in range(0,len(backitems))]

# 获取k3
def get_k3(k1, k2):
    for k3 in range(0,26):
        if k3 * k1 % 26 == 1:
            return k3

# 判断一个数是否是整数
def is_int(n):
    int_n = int(n)
    return n * n == int_n * int_n

# 仿射解密过程
def FsJM(c, k1, k2):
    k3 = get_k3(k1, k2)
    Ms = ""
    for x in c:
        Ms = Ms + get_char_by_int( k3 * (get_int_by_char(x) - k2) % 26 )
    return Ms

# 根据a，b，c，d获取密钥K1
def get_k1(a, b, c, d):
    i = 0
    while True:
        k1 = ( float(a - d - 26 * i) / float(b - c) )
        if k1 < -26 or k1 > 26:
            return None
        if is_int(k1):
            return int(k1)
        i = i + 1

Cs = filter( del_point, Cs.lower() )
count = {}

for v in Cs:
    count[v] = count[v] + 1 if count.has_key(v) else 1

sortCs = map(get_int_by_char,sort_by_value(count))

# 精度
prec = 4
result = []
for a in sortCs[0:len(sortCs)/prec]:
    for b in frequencyTable[0:len(frequencyTable)/prec]:
        for c in frequencyTable[frequencyTable.index(b) + 1:len(frequencyTable)/prec]:
            for d in sortCs[sortCs.index(a)+1:len(sortCs)/prec]:
                k1 = get_k1(a, b, c, d)
                if k1 is None or gcd(k1, 26) != 1:
                    break
                k2 = int(d - c * k1) % 26
                result.append( (k1, k2, FsJM(Cs, k1, k2)) )

for val in result:
    print val
