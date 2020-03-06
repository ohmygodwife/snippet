'''
p+1/p-1 smooth, ONLY works in Linux
$ python -m primefac -vs -m=p+1  149767527975084886970446073530848114556615616489502613024958495602726912268566044330103850191720149622479290535294679429142532379851252608925587476670908668848275349192719279981470382501117310509432417895412013324758865071052169170753552224766744798369054498758364258656141800253652826603727552918575175830897
openssl rsa -pubin -in pubkey.pem -text -modulus
openssl rsa -in privkey.pem -text -modulus
openssl genrsa -out privkey.pem 1024 #Generating RSA private key, 1024 bit long modulus
openssl rsautl -decrypt -inkey privkey.pem -in cipher.bin
openssl x509 -in certificate.der -inform der -text
openssl x509 -noout -text -in .\public.cer
# cipher.bin must be convert to HEX first(https://stackoverflow.com/questions/12191045/openssl-rsa-private-decrypt-error0406506clib4func101reason108/12295167)
'''
from Crypto import Random
import gmpy2
import libnum
import base64
from Crypto.PublicKey import RSA

#a, b = gmpy2.iroot(cipher + j * N, 3)

def rawDecrypt():
  n = 124505798868852368271793067207129696073932674127432142354942921070883060568367994640569010231335260457364506494110523026110017140104859164273763238997103561724449631734026588389430139126071592845163714736995224119505578368149365211675712937016546150619119982582497478157517451465975193671664573708353622373359L
  qminusp = 3076433822814954379524766401149703829388998303211949802495903993728411768630234941908379224548551637739711829408802249649539193280247277641130590337304610L
  halfqminusp = qminusp/2
  middle, b = gmpy2.iroot(n + halfqminusp ** 2, 2)
  p = middle - halfqminusp
  q = middle + halfqminusp
  e = 0x10001
  c =  105702092942480216808987947180348159712934515048625475079443402060719559982175270811740635796620474013214290280844589887665491447050031281746238320223842507876814558068400743520403677184631212452385840444660554121661227109633578670985114753142834784623644362967835816416843246404222481675851140132182188823299L

  phin = (p - 1) * (q - 1)
  d = gmpy2.invert(e, phin)
  m = gmpy2.powmod(c, d, n)
  h = hex(m)
  print h
  print h[h.index('66') : h.index('7d') + 2].decode('hex')
  
rawDecrypt()



#A tuple of long integers, with at least 2 and no
#more than 6 items. The items come in the following order:
#1. RSA modulus (n).
#2. Public exponent (e).
#3. Private exponent (d). Only required if the key is private.
#4. First factor of n (p). Optional. If None, compute factors p and q from the private exponent d. See _slowmath.rsa_construct
#5. Second factor of n (q). Optional.
#6. CRT coefficient, (1/p) mod q (u). Optional.
def rsaDecrypt():
  n = 322831561921859
  p = 13574881
  q = 23781539
  e = 23
  rsa = RSA.construct((n, long(e), long(gmpy2.invert(e, (p - 1) * (q - 1)))))
  c = libnum.n2s(0xdc2eeeb2782c)
  print rsa.decrypt(c)

#rsaDecrypt()  



#: A public key will only have the following entries:
    #:  - **n**, the modulus.
    #:  - **e**, the public exponent.
#: A private key will also have:
    #:  - **d**, the private exponent.
    #:  - **p**, the first factor of n.
    #:  - **q**, the second factor of n.
    #:  - **u**, the CRT coefficient (1/p) mod q.
def importPublicPem():
  f = open('pubkey.pem','r')
  rsa = RSA.importKey(f.read())
  print "n=" , rsa.n
  print "e=" , rsa.e

#importPublicPem()




def pemDecrypt():
  f = open('privkey.pem','r')
  rsa = RSA.importKey(f.read())
  print "n=" , rsa.n
  print "e=" , rsa.e
  print "d=" , rsa.d
  print "p=" , rsa.p
  print "q=" , rsa.q
  c = "wYGRA2p+TzMsgUD31oD5qSvutHm68jxDXQSgLVQR4eiUlPhWAcuB4SsSpoDAgz+ykqEGpV8jk9ljLk4qSvOCNcNMeTIsO9ybvkmiw4oic7kr2L2r6VUYRtt5ZTQvXCrtDvdLvKQUZb4lI+QvkSggoju5BplNWCzLwaaUXz5SjPQtFh9No5NtsL4R2FvJ+rR1/F8ulfzPOWgSvOo6/QUykymy6ha6EisVLipDjjzjJwHNH3IRkLJd2FWkU2GjBps0KfOFoPZZWJ+T7Onhn85ll0/qNejD1Em6zaMiX5YE/YoXi9meT05MUeuZIbd7aqqDduUYIw3hs/ekAhDtUBdhmg=="
  c = base64.b64decode(c)
  print rsa.decrypt(c)

#pemDecrypt()




def generate():
  random_generator = Random.new().read
  rsa = RSA.generate(1024, random_generator) #if random_generator is None, it would instantiate one from Crypto.Random also
  #generate private/public according to whether the key contains "d"
  #def has_private(self):
  #      return hasattr(self, 'd')
  open('./privkey.pem', 'w').write(rsa.exportKey('PEM'))



  
def getGcd(n):
  for i in range(len(n)):
    for j in range(i+1, len(n)):
      p = gmpy2.gcd(n[i], n[j])
      if p > 1 :
        return p, i , j

def nNotCoprime():
  n = []
  c = []
  with open("topic.txt") as f:
    for line in f:
      if line.startswith('e = '):
        e = int(line[4:])
      elif line.startswith('n = '):
        x = int(line[4:])
        n.append(x)
      elif line.startswith('c = '):
        x = int(line[4:])
        c.append(x)

  p,i,j = getGcd(n)
  print p, i, j
  q = n[i] / p
  phin = (p - 1) * (q - 1)
  d = gmpy2.invert(e, phin)
  plain = gmpy2.powmod(c[i], d, n[i])
  print libnum.n2s(plain)


def convDec(plain):
  i = 0
  flag = ""
  plain = str(plain)
  while i < len(plain):
    if plain[i] == '1':
      flag += chr(int(plain[i:i + 3]))
      i += 3
    else:
      flag += chr(int(plain[i:i + 2]))
      i += 2
  print flag
  
#convDec(1021089710312311910410111011910111610410511010710511610511511211111511510598108101125)

def sameN():
  n = 6266565720726907265997241358331585417095726146341989755538017122981360742813498401533594757088796536341941659691259323065631249
  e1 = 773
  e2 = 839

  message1 = 3453520592723443935451151545245025864232388871721682326408915024349804062041976702364728660682912396903968193981131553111537349

  message2 = 5672818026816293344070119332536629619457163570036305296869053532293105379690793386019065754465292867769521736414170803238309535
  # s & t
  gcd, s, t = gmpy2.gcdext(e1, e2)
  if s < 0:
    s = -s
    message1 = gmpy2.invert(message1, n)
  if t < 0:
    t = -t
    message2 = gmpy2.invert(message2, n)
  plain = gmpy2.powmod(message1, s, n) * gmpy2.powmod(message2, t, n) % n
  print plain
  convDec(plain)

#sameN()

def e3Brute():
  n=0x7003581fa1b15b80dbe8da5dec35972e7fa42cd1b7ae50a8fc20719ee641d6080980125d18039e95e435d2a60a4d5b0aaa42d5c13b0265da4930a874ddadcd9ab0b02efcb4463a33361a84df0c02dfbd05c0fdc01e52821c683bd265e556412a3f55e49517778079cb1c1c1c22ef8a6e0bccd5e78888ff46167a471f6bff25664a34311c5cb8d6c1b1e7ac2ab0e6676d594734e8f7013b33806868c151316d0cf762a50066c596244fd70b4cb021369aae432e174da502a806e7a8ab13dad1f1b83ac73c0e9e39648630923cbd5726225f17cc0d15afadb7d2c2952b6e092ffc53dcff2914bfddedd043bbdf9c6f6b6b5a6269c5bd423294b9deac4f268eaadb
  e=0x3
  c=0xb2ab05c888ab53d16f8f7cd39706a15e51618866d03e603d67a270fa83b16072a35b5206da11423e4cd9975b4c03c9ee0d78a300df1b25f7b69708b19da1a5a570c824b2272b163de25b6c2f358337e44ba73741af708ad0b8d1d7fa41e24344ded8c6139644d84dc810b38450454af3e375f68298029b7ce7859f189cdae6cfaf166e58a22fe5a751414440bc6bce5ba580fd210c4d37b97d8f5052a69d31b275c53b7d61c87d8fc06dc713e1c1ce05d7d0aec710eba2c1de6151c84d7bc3131424344b90e3f8947322ef1a57dd3a459424dd31f65ff96f5b8130dfd33111c59f3fc3a754e6f98a836b4fc6d21aa74e676f556aaa5a703eabe097140ec9d98

  i = 0
  while True:
    if iroot(c + i * n, 3)[1] == True:
        print i
        print "Success!"
        print hex(iroot(c + i * n, 3)[0])
        break
    i += 1

#e3Brute()

import scryptos

def chinese_remainder(a, n):
    sum = 0
    prod = reduce(lambda a, b: a * b, n) #sequentially apply a*b to list n
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * gmpy2.invert(p, n_i) * p
    return int(sum % prod)

def broadcast():
  e=3    
  n=[0x43d819a4caf16806e1c540fd7c0e51a96a6dfdbe68735a5fd99a468825e5ee55c4087106f7d1f91e10d50df1f2082f0f32bb82f398134b0b8758353bdabc5ba2817f4e6e0786e176686b2e75a7c47d073f346d6adb2684a9d28b658dddc75b3c5d10a22a3e85c6c12549d0ce7577e79a068405d3904f3f6b9cc408c4cd8595bf67fe672474e0b94dc99072caaa4f866fc6c3feddc74f10d6a0fb31864f52adef71649684f1a72c910ec5ca7909cc10aef85d43a57ec91f096a2d4794299e967fcd5add6e9cfb5baf7751387e24b93dbc1f37315ce573dc063ecddd4ae6fb9127307cfc80a037e7ff5c40a5f7590c8b2f5bd06dd392fbc51e5d059cffbcb85555, 0x60d175fdb0a96eca160fb0cbf8bad1a14dd680d353a7b3bc77e620437da70fd9153f7609efde652b825c4ae7f25decf14a3c8240ea8c5892003f1430cc88b0ded9dae12ebffc6b23632ac530ac4ae23fbffb7cfe431ff3d802f5a54ab76257a86aeec1cf47d482fec970fc27c5b376fbf2cf993270bba9b78174395de3346d4e221d1eafdb8eecc8edb953d1ccaa5fc250aed83b3a458f9e9d947c4b01a6e72ce4fee37e77faaf5597d780ad5f0a7623edb08ce76264f72c3ff17afc932f5812b10692bcc941a18b6f3904ca31d038baf3fc1968d1cc0588a656d0c53cd5c89cedba8a5230956af2170554d27f524c2027adce84fd4d0e018dc88ca4d5d26867, 0x280f992dd63fcabdcb739f52c5ed1887e720cbfe73153adf5405819396b28cb54423d196600cce76c8554cd963281fc4b153e3b257e96d091e5d99567dd1fa9ace52511ace4da407f5269e71b1b13822316d751e788dc935d63916075530d7fb89cbec9b02c01aef19c39b4ecaa1f7fe2faf990aa938eb89730eda30558e669da5459ed96f1463a983443187359c07fba8e97024452087b410c9ac1e39ed1c74f380fd29ebdd28618d60c36e6973fc87c066cae05e9e270b5ac25ea5ca0bac5948de0263d8cc89d91c4b574202e71811d0ddf1ed23c1bc35f3a042aac6a0bdf32d37dede3536f70c257aafb4cfbe3370cd7b4187c023c35671de3888a1ed1303]
  c=[0x5517bdd6996b54aa72c2a9f1eec2d364fc71880ed1fa8630703a3c38035060b675a144e78ccb1b88fa49bad2ed0c6d5ad0024d4bb18e7d87f3509b0dbf238a0d1ff33f48ffc99c1bdf2f2547a193e7ab66eec562a7bc3f9521f70d453ff6d1fdb24de40b3f621ca6be6606440d09d0f302d5806e7cebc9b612522f181baa43373d6827ffd794916ffcc205147c8d88a59d2fce4bbcdfd6a4934fb72d5f74be79a1bd64b4305865c9d20eb96d8bd7976440a4bc326fdb5b9a04bac3762a664346a175f1029f448bb421506f3dfeb75d6531f89f0b92a7e66e295ede5928ec8301a202d5c9fd528cda84190c2b47f423af1a59c63ae6253d1903c83ae158f9b42, 0x3288e3ea8c74fd004e14b66a55acdcbcb2e9bd834b0f543514e06198045632b664dac3cf8578cde236a16bef4a1246de692ec6a61ce507a220fa04e09044632787ba42b856cb13be6e905c20b493004822888d3c44c6fc367c7af0287f1683f08baae5bb650902067908e93246af3954d62437aa14248529fd07c8902b9403920b6550f12d1c398881cd7fc8b5f096f38c33df21887bfe989fb011a9deade2370d90347510b76f1f3e3dedf09c148675ea8919878c8ac188253b78886d906cd1f3aee5484d6d13fb4bbad233f670f825fa618adbf0705ed4e31b60957f5c28cfd1febd13370630a6c94990e341d38918a9c1faa614fd14cdd41b7bc8461f2f0c, 0xb0c5ee1ac47c671c918726287e70239147a0357a9638851244785d552f307ed6a049398d3e6f8ed373b3696cfbd0bce1ba88d152f48d4cea82cd5dafd50b9843e3fa2155ec7dd4c996edde630987806202e45821ad6622935393cd996968fc5e251aa3539ed593fe893b15d21ecbe6893eba7fe77b9be935ca0aeaf2ec53df7c7086349eb12792aefb7d34c31c18f3cd7fb68e8a432652ef76096096e1a5d7ace90a282facf2d2760e6b5d98f0c70b23a6db654d10085be9dcc670625646a153b52c6c710efe8eb876289870bdd69cb7b45813e4fcfce815d191838926e9d60dd58be73565cff0e10f4e80122e077a5ee720caedc1617bf6a0bb072bbd2dab0]

  m_e = libnum.solve_crt(c,n)#scryptos.crt(c, n) #chinese_remainder(ak, nk)
  m = gmpy2.iroot(m_e, e)
  if m[1]:
    print m[0]

#broadcast()

def eNotCoprimePhi():
  c = 2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524
  n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067
  e = 3

  p1 = 32581479300404876772405716877547
  p2 = 27038194053540661979045656526063
  p3 = 26440615366395242196516853423447

  c1 = eval(scryptos.parigp(["Vec(liftall(sqrtnall(Mod(%d, %d), 3)))" % (c, p1)]))
  c2 = eval(scryptos.parigp(["Vec(liftall(sqrtnall(Mod(%d, %d), 3)))" % (c, p2)]))
  c3 = eval(scryptos.parigp(["Vec(liftall(sqrtnall(Mod(%d, %d), 3)))" % (c, p3)]))
  print c1, c2, c3

  #c1 = [6149264605288583791069539134541, 13404203109409336045283549715377, 13028011585706956936052628027629]
  #c2 = [19616973567618515464515107624812]
  #c3 = [13374868592866626517389128266735, 7379361747422713811654086477766, 5686385026105901867473638678946]


  for x in c1:
    for y in c2:
      for z in c3:
        m = libnum.solve_crt([x,y,z], [p1,p2,p3]) #chinese_remainder(ak, nk)
        d = libnum.n2s(m)
        if "0ctf" in d:
          print d[d.find("0ctf"):].strip()

#eNotCoprimePhi()

def e3SameNLinearM(a, b, c1, c2, n):
  a3 = gmpy2.powmod(a, 3, n)
  b3 = gmpy2.powmod(b, 3, n)
  part1 = b * (c1 + 2 * a3 * c2 - b3) % n
  part2 = a * (c1 - a3 * c2 + 2 * b3) % n
  part2 = gmpy2.invert(part2, n)
  return part1 * part2 % n

def callE3SameNLinearM():
  id1 = 1002
  id2 = 2614
  c1 = 0x547995f4e2f4c007e6bb2a6913a3d685974a72b05bec02e8c03ba64278c9347d8aaaff672ad8460a8cf5bffa5d787c5bb724d1cee07e221e028d9b8bc24360208840fbdfd4794733adcac45c38ad0225fde19a6a4c38e4207368f5902c871efdf1bdf4760b1a98ec1417893c8fce8389b6434c0fee73b13c284e8c9fb5c77e420a2b5b1a1c10b2a7a3545e95c1d47835c2718L
  c2 = 0x547995f4e2f4c007e6bb2a6913a3d685974a72b05bec02e8c03ba64278c9347d8aaaff672ad8460a8cf5bffa5d787c72722fe4fe5a901e2531b3dbcb87e5aa19bbceecbf9f32eacefe81777d9bdca781b1ec8f8b68799b4aa4c6ad120506222c7f0c3e11b37dd0ce08381fabf9c14bc74929bf524645989ae2df77c8608d0512c1cc4150765ab8350843b57a2464f848d8e08L
  n = 25357901189172733149625332391537064578265003249917817682864120663898336510922113258397441378239342349767317285221295832462413300376704507936359046120943334215078540903962128719706077067557948218308700143138420408053500628616299338204718213283481833513373696170774425619886049408103217179262264003765695390547355624867951379789924247597370496546249898924648274419164899831191925127182066301237673243423539604219274397539786859420866329885285232179983055763704201023213087119895321260046617760702320473069743688778438854899409292527695993045482549594428191729963645157765855337481923730481041849389812984896044723939553
  a = 1
  b = id1 - id2
  m2 = e3SameNLinearM(a, b, c1, c2, n) - id2
  print libnum.n2s(m2)
  
#callE3SameNLinearM()
    
import primefac
def factorN():
  n = 322831561921859
  factors = primefac.primefac(n)
  list = map(str, factors)
