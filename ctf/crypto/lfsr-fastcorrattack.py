#zer0lfsr, 0ctf-2019, http://igml.top/2019/03/28/2019-0CTF/, https://www.anquanke.com/post/id/184828
import libnum

with open('keystream', 'rb') as f:
  data = f.read()
  data = data.decode('utf-8')
  print len(data)
  bits = libnum.s2b(data)

probabilities = [0.75, 0.75, 0.75] 
masks = ['100000000000000000000000010000000000000000000000', '100000000000000000000000000000000010000000000000', '100000100000000000000000000000000000000000000000']
len_mask = len(masks[0])

def get_mask_indexes(mask, length):
  arr = []
  start = 0
  while True:
    start = mask.find('1', start)
    if start == -1:
      break
    arr.append(length - start)
    start += 1
  return arr[::-1]

def gen_init():
  for i in range(len(masks)):
    arr = get_mask_indexes(masks[i], len_mask)
    with open('init{}'.format(i), 'w') as f:
      f.write('{}\n{}\n{}\n{}\n'.format(probabilities[i], len(bits), len_mask, len(arr)))
      for j in arr:
        f.write('{}\n'.format(j))
      f.write(bits)

#step1: 
gen_init()
#step2: /mnt/hgfs/tools/crypto/lfsr-fast-correlation-attack/src/fca init0 > out0
#step3: lfsr_inv each

key  = ['100100011111111010101110010010110100101000110011', '001101101101101111001001101101110000001001000011', '001000101001101100100001101111101011101010100001']

def lfsr(R,mask):
    output = (R << 1) & 0xffffffff
    i=(R&mask)&0xffffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1) #lastbit = lastbit + i & 1
        i=i>>1
    output^=lastbit
    return (output,lastbit)

def lfsr_inv(R,mask):
    lengthmask = 2**(len_mask)-1
    rr=R.rjust(len_mask, '0')
    new=rr[-1]+rr[:-1]  #ror
    new=int(new,2)
    i = new & int(mask, 2) & lengthmask
    lastbit = 0
    while i != 0:
        lastbit ^= (i & 1)
        i = i >> 1
    return '{}'.format(lastbit) + R[:-1]

for i in range(len_mask):
  for j in range(len(masks)):
    key[j] = lfsr_inv(key[j], masks[j])

flag = ''
for i in key:
  flag += libnum.b2s(i)

import hashlib

print hashlib.sha256(flag).hexdigest()
