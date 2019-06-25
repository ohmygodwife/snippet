'''https://www.cnblogs.com/s1ye/p/9021202.html
E2 xor C1 = P2
E2 xor C1_new = P2_new (target: admin for instance)
C1_new = C1 xor P2 xor P2_new

E1 xor IV = P1_new (need to fetch by C1_new)
E1 xor IV_new = P1
IV_new = IV xor P1_new xor P1 
'''

iv='235d5e78277087a9cb82b8ea0ca94a47'.decode('hex')
cipher='4721f1a3f57ed3d6fcad72461fa548157948d1a3ae1df22e165128c82b6e2e59a5634cb04f7a4ffb5853e8b6213ab936c18dedabd8bd22cb4a9dd22c283f0710'.decode('hex')
plain='7b27757365726e616d655f5f273a202741646d696e272c20276c6f67696e5f74696d655f5f273a20313534333037393135302e3431383730397d303030303030'.decode('hex')

new_cipher = chr(ord(cipher[0]) ^ ord('A') ^ ord('a')) + cipher[1:]
print new_cipher.encode('hex')

#input original iv and new cipher to get new plain
new_plain = 'd7f3dc9f7c31d2b7d1d4a092f13a3b6b'.decode('hex')

new_iv = ''
for i in range(len(iv)):
  new_iv += chr(ord(iv[i]) ^ ord(plain[i]) ^ ord(new_plain[i]))

print new_iv.encode('hex')

'''
{'username__': '
Admin', 'login_t
ime__': 15430761
24.083409}000000
'''
'''
#-*- coding:utf8 -*-
import base64
import urllib
# a:2:{s:8:"userna
# me";s:5:"admiN";
# s:8:"password";s
# :6:"123456";}
 
def Module1():
    ciphertext = raw_input("Please input the first round cipher:\n")
    cipher = base64.b64decode(urllib.unquote(ciphertext))
    new_cipher = cipher[:13] + chr(ord(cipher[13]) ^ ord('N') ^ ord('n')) + cipher[14:]
    print urllib.unquote(base64.b64encode(new_cipher))
 
def Module2():
    errorcipher = base64.b64decode(urllib.unquote(raw_input('Please input errorcipher: \n')))
    ivtext = raw_input("Please input iv:\n")
    iv = base64.b64decode(urllib.unquote(ivtext))
    cleartext = 'a:2:{s:8:"userna'
    newiv = ''
    for i in range(16):
        newiv += chr(ord(iv[i]) ^ ord(errorcipher[i]) ^ ord(cleartext[i]))
    print urllib.unquote(base64.b64encode(newiv))
 
option = raw_input("Please input option [1 or 2]:")
if option == '1':
    Module1()
elif option == '2':
    Module2()
else:
    pass
    
'''