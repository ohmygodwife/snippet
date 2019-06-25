'''
openssl dgst -sha1 -sign dsa_private.pem -out sign.bin message.txt #sign
openssl sha1 -verify dsa_public.pem -signature sign.bin message.txt #verify
openssl dsa -in dsa_public.pem -text -noout -pubin #read public pem file
openssl asn1parse -inform der -in packet4/sign4.bin #read r and s from sign file
'''
#coding=utf8
from Crypto.PublicKey import DSA
from hashlib import sha1,md5
import gmpy2

with open('./dsa_public.pem') as f:
    key = DSA.importKey(f)
    y = key.y
    g = key.g
    p = key.p
    q = key.q

def sameR():
  f3 = open(r"packet3/message3", 'r')
  f4 = open(r"packet4/message4", 'r')
  data3 = f3.read()
  data4 = f4.read()
  sha = sha1()
  sha.update(data3)
  m3 = int(sha.hexdigest(), 16)
  sha = sha1()
  sha.update(data4)
  m4 = int(sha.hexdigest(), 16)
  print m3, m4
  s3 = 0x1B474F2C1C9E85B72841AD84D9A871A11EF0F323
  s4 = 0x0EA21858C18AA1EDF4058B6EB9E02B0176243658
  r = 0x12E780EE8471DC3552572BB6E818F6D22CE16EA4
  #k(s1-s2) = H(m1)-H(m2) mod q
  ds = s4 - s3
  dm = m4 - m3
  k = gmpy2.mul(dm, gmpy2.invert(ds, q))
  k = gmpy2.f_mod(k, q)
  #x = r^(-1) * (ks-H(m)) mod q
  tmp = gmpy2.mul(k, s3) - m3
  x = tmp * gmpy2.invert(r, q)
  x = gmpy2.f_mod(x, q)
  print hex(x)

sameR()