n=1
last = matrix(ZZ,[[1]*n])
# open the public key and strip the spaces so we have a decent array
fileKey = r'''60576
45547
48645
60358
60779
44939
48653
44306
46781
57823'''
pubKey = fileKey.replace(' ', '').replace('L','').split('\n')
#pubKey = open("pub.Key", 'r').read().replace(' ', '').replace('L', '').strip('[]').split(',')
pubKey = [int(i) for i in pubKey]
print(pubKey)
nbit = len(pubKey)
# open the encoded message
fileEnc = r'''260486'''
encoded = int(fileEnc.replace('L',''))
#encoded = open("enc.txt", 'r').read().replace('L', '')
print(encoded)

#https://ctf-wiki.github.io/ctf-wiki/crypto/asymmetric/knapsack/knapsack-zh/
def LLL0(pubKey, encoded):
  # create a large matrix of 0's (dimensions are public key length +1)
  A = Matrix(ZZ,nbit+1,nbit+1)
  # fill in the identity matrix
  for i in range(nbit):
      A[i,i] = 1
  # replace the bottom row with your public key
  for i in range(nbit):
      A[i,nbit] = pubKey[i]
  # last element is the encoded message
  A[nbit,nbit] = -int(encoded)

  res = A.LLL()
  print(res)
  print(res[0][:-1]) #need to remove last 0 element!
print('LLL0')
LLL0(pubKey, encoded)

#https://badmonkey.site/archives/2020-5-dasctf.html
def LLL1(publickey, enc):
    n = len(publickey)
    d = 2*identity_matrix(QQ,n,n)
    col = publickey+[enc]
    col = matrix(col).transpose()
    last = matrix(ZZ,[[1]*n])
    tmp = block_matrix(ZZ,[[d],[last]])
    grid = block_matrix(ZZ,[[tmp,col*(1^300)]])
    M = grid.LLL()
    print(M)

print('LLL1')
LLL1(pubKey, encoded)

#https://shimo.im/docs/DRgjXTH3cJjrHKcw
def LLL2(data, s):
    n = len(data)
    A = Matrix(QQ, n + 1)
    for i in range(n):
        A[i, i] = 2
    for i in range(n):
        A[n, i] = 1
    for i in range(n):
        A[i, n] = n * data[i]
    A[n, n] = n * s
    B = A.LLL()
    print(B)
print('LLL2')
LLL2(pubKey, encoded)


