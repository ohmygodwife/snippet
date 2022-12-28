#!/usr/bin/python
import libnum, decimal
from pwn import *
# from ./lsb_oracle.vmp.exe /pubkey
n = 120357855677795403326899325832599223460081551820351966764960386843755808156627131345464795713923271678835256422889567749230248389850643801263972231981347496433824450373318688699355320061986161918732508402417281836789242987168090513784426195519707785324458125521673657185406738054328228404365636320530340758959
e = 65537
# from description.py
c = 2201077887205099886799419505257984908140690335465327695978150425602737431754769971309809434546937184700758848191008699273369652758836177602723960420562062515168299835193154932988833308912059796574355781073624762083196012981428684386588839182461902362533633141657081892129830969230482783192049720588548332813
# Encrypt the plaintext integer 2
c_of_2 = pow(2,e,n)
# Run the oracle in wine. Works fine. Who needs windows.
p = process(['wine','lsb_oracle.vmp.exe','/decrypt'])
print "[*] Starting wine and LSB Oracle..."
p.recvlines(4)
# Ask the oracle for the LSB of a decryption of c
def oracle(c):
    p.sendline(str(c))
    return int(p.recvlines(2)[0])
# code from http://secgroup.dais.unive.it/wp-content/uploads/2012/11/Practical-Padding-Oracle-Attacks-on-RSA.html 
# by Riccardo Focardi
def partial(c,n):
    k = n.bit_length()
    decimal.getcontext().prec = k    # allows for 'precise enough' floats
    lower = decimal.Decimal(0)
    upper = decimal.Decimal(n)
    for i in range(k):
        possible_plaintext = (lower + upper)/2
        c=(c*c_of_2) % n     # multiply y by the encryption of 2 again
        lsb = oracle(c)
        if not lsb: #lsb is 0
            upper = possible_plaintext            # plaintext is in the lower half
        else:
            lower = possible_plaintext            # plaintext is in the upper half
        
        print i, lsb, int(upper - lower)
    # By now, our plaintext is revealed!
    return int(upper)
print "[*] Conducting Oracle attack..."
print repr(libnum.n2s(partial(c,n)))