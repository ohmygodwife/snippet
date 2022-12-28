#https://www.cnblogs.com/zhanp/p/10931617.html

import libnum

def conv(s):
  return hex(int(s,2))[2:]

#https://mp.weixin.qq.com/s/C7MohZk3jF3Zb_V4wYlYoQ, redhat-2018
def manchester():
  n=0x123654AAA678876303555111AAA77611A321
  flag=''
  
  bs='0'+bin(n)[2:]
  print bs
  r=''
  for i in range(0,len(bs),2):
    if bs[i:i+2]=='01': # 0->1 means 0, 1->0 means 1; or 01 means 1, 10 means 0
      r+='0'
    else:
      r+='1'
  print r
  for i in range(0,len(r),8):
    tmp=r[i:i+8][::-1]
    flag+=conv(tmp[:4])
    flag+=conv(tmp[4:])
  
  print("flag"+"{"+flag.upper()+"}")

manchester()

#key, wdb-2020-3rd, https://y-y-k.tk/2020/05/18
def diff_manchester():
  n = 0x295965569a596696995a9aa969996a6a9a669965656969996959669566a5655699669aa5656966a566a56656
  bs = bin(n)[2:]
  print bs
  print len(bs)
  
  r = ''
  for i in range(2,len(bs),2):
    if bs[i]==bs[i-1]: # 0101,1010 1->0,0->1 change means 0; 0110,1001 unchange means 1
      r+='1'
    else:
      r+='0'
  
  print r
  
  print libnum.b2s(r)
  
diff_manchester()  
  
  
def wp():
  enc = '295965569a596696995a9aa969996a6a9a669965656969996959669566a5655699669aa5656966a566a56656'
  s = ''
  for c in enc:
    s += '{:04b}'.format(int(c, 16))
    
  s = s[2:]
  print s
  print len(s)
  r = ''
  for i in range(1, len(s) // 2):
    if s[i*2] == s[i*2 - 1]:
      r += '1'
    else:
      r += '0'
      
  print r
  print libnum.b2s(r)
wp()
  
