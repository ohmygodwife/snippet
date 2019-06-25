'''
equation,0ctf-2016
http://www.vuln.cn/6004
https://0day.work/0ctf-2016-quals-writeups/
http://mslc.ctf.su/wp/0ctf-2016-quals-equation-crypto-2-pts/
https://grocid.net/2016/03/14/0ctf-equation/
'''

import gmpy2

e = 65537 #assume

privkey = '''Os9mhOQRdqW2cwVrnNI72DLcAXpXUJ1HGwJBANWiJcDUGxZpnERxVw7s0913WXNt
V4GqdxCzG0pG5EHThtoTRbyX0aqRP4U/hQ9tRoSoDmBn+3HPITsnbCy67VkCQBM4
xZPTtUKM6Xi+16VTUnFVs9E4rqwIQCDAxn9UuVMBXlX2Cl0xOGUF4C5hItrX2woF
7LVS5EizR63CyRcPovMCQQDVyNbcWD7N88MhZjujKuSrHJot7WcCaRmTGEIJ6TkU
8NWt9BVjR4jVkZ2EqNd0KZWdQPukeynPcLlDEkIXyaQx'''.replace('\n', '')
print privkey.decode('base64').encode('hex')

lowbit_q = 0x3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b

d_p = 0xd5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed59
d_q = 0x1338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3

invert_q_mod_p = 0x00d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431

for k_q in range(1, e):
    if (e*d_q - 1) % k_q == 0:
        q = (e*d_q - 1) / k_q + 1
        if q % (2**lowbit_q.bit_length()) == lowbit_q:
        #if hex(q).endswith(hex(lowbit_q)[2:]):
            print '[q] {}'.format(q)
            break

for k_p in range(1, e):
    if (e*d_p - 1) % k_p == 0:
        p = (e*d_p - 1) / k_p + 1
#        if gmpy2.is_prime(p):
        if gmpy2.invert(q, p) % p == invert_q_mod_p:
            print '[p] {}'.format(p)
            break


kp = q * invert_q_mod_p - 1 # q * invert(q, p) = k * p + 1
xp =  pow (2, e * d_p, kp) - 2 # 2 ^ (e * d_p) = 2 mod p = g * p + 2, it should mod p, but here just mod kp instead, g*p % k*p = x*p
yp = gmpy2.gcd(xp, kp)
p = yp / 10 # factor xp, easy to find: xp = 2 * 5 * p
print '[p] {}'.format(p)

#e*d_p = x*(p-1)+1 -> e*d_p-1 = x*p-x -> e*d_p-1+x = x*p
for x in range(1, e):
  p = gmpy2.gcd(e*d_p - 1 + x, kp)
  if p.bit_length() >= d_p.bit_length():
    print '[p] {}'.format(p)
    break

# [p] 12883429939639100479003058518523248493821688207697138417834631218638027564562306620214863988447681300666538212918572472128732943784711527013224777474072569
# [q] 12502893634923161599824465146407069882228513776947707295476805997311776855879024002289593598657949783937041929668443115224477369136089557911464046118127387