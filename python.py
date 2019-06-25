# -*- coding: utf-8 -*-
'''Sample code.

small samples'''
if __name__ == '__main__':
  main()
  
x += 256 if v_flag else 1 #if True plus 256, else plus 1

#string operation#######################################################
print(ord('a')) #ch -> int
print(chr(97))  #int -> ch
str='''
"What's your name?," I asked.
He said "Bond, James Bond."
''';
print('{0} was {1:.3f} years old when he wrote this book'.format(str, 1.0/3))
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print(r"Newlines are indicated by \n") #Raw string
print "%#x => %s" % (address, (data or '').encode('hex'))
x = b'%.4x' % i #to hex with prefix 0
b = '{:08b}'.format(a) # to bin with prefix 0

''.join(flag) #flag is a char list
start = line.find('private_bit : 1,')
m1 = re.search("01/Mar/2015:13:\d{2}:(\d{2})", list[i])
t1 = m1.group(1)
str.lower()
str.upper()

from Crypto.Util import number
number.long_to_bytes(0x4342) #CB
number.bytes_to_long('hello') #448378203247=0x68656c6c6f
number.size(0x1234) #print bit length
for p in number.sieve_base:
  print p #The first 10000 primes

json.dumps(data) # Encode the data
json.loads(in_json) # Decode into a Python object

#https://blog.csdn.net/w83761456/article/details/21171085
#https://docs.python.org/3/library/struct.html
struct.pack('>i', 0x121212) #> big endian, < little endian, h:2byte, i/l:4byte, q:8byte, f:4byte float, d:8byte double
a,=struct.unpack('>i', '1234')#Note: unpack returns tuple !!
struct.pack('5s6s2if',a,b,c,d,e) #5s: 5bytes string,2i: 2 4bytes integer

def rot13(message):
  first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
  return message.translate(string.maketrans(first, trance)) 

table = string.maketrans("NoPqRsTuVwXyZaBcDeFgHiJkLm567234", "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") #base32
table = string.maketrans("BACDEFGHIJSTUVWKLMNOPQRXYZabcdqrstuvwxefghijklmnopyz0123456789+/", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/") #base64
EnBase32 = "weNTDk5LZsNRHk6cVogqTZmFy2NRP7X4ZHLTBZwg".translate(table)

if all([c in string.printable for c in str]): #all element satisfy

for i in (N,e,c):
  print list(collections.Counter(i)) #statistic char count

print libnum.n2s(flag) #int to string
print libnum.b2s(flag) #bin to string

########################################################################
#list: Mutable []
list = [0 for x in range(0, 1000)]
listtwo = [2*i for i in listone if i > 2] #listone = [2, 3, 4]
array = [chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in xrange(len(a))]
array = [[False for col in range(59)] for row in range(22)] #arr[22][59]
nArr = [-1]*e

array.reverse() == array[::-1]  #reverse a list or a string
list1.extend(list2) #append all elements in list2 to list1
shoplist.sort() #change in list itself
shoplist.remove('carrot')
del shoplist[0]

# Lambda
points = [{'x': 2, 'y': 3},
{'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])   # Sort by 'y'?
print(points)

# map apply function to every element in list
data = list(map(lambda x: list(map(lambda y: int(y, 16), x.split(":"))), open("data").read().splitlines()))

#deep copy
mylist = shoplist[:]    #clone by slicing
import copy
mylist = copy.deepcopy(shoplist) #deep copy
mylist = copy.copy(shoplist) #shallow copy

a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b) #[(1, 4), (2, 5), (3, 6)]

#tuple: Immutable ()
zoo = ('python', 'elephant', 'penguin')
zooList = list(zoo) #tuple to list

#dict {}
ab = {'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org'} #dict
dict1.update(dict2) #update dict1 with dict2 elements, the value for same key in dict1 would be replaced.
del ab['Larry']
for name, address in ab.items(): #ab.keys()/ab.values()/ab.has_key()
    print('Contact {} at {}'.format(name, address))

#set
bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri & bric)

########################################################################
# default open file with 'r'(read) and 't'(text)
with open("poem.txt", "rb") as f: # auto close file, like try-resource in Java
  for line in f:
    print(line)

list = f.readlines()
f.writelines(list)
f.seek(off, whence=0) #whence = 0:start, 1:current, 2:end
pos = f.tell()
f.close()

import pickle   #serialize
pickle.dump(shoplist, f) #Dump the object to a file
storedlist = pickle.load(f) #Load the object from the file

#encoding
f = io.open("abc.txt", "wt", encoding="utf-8")
text = io.open("abc.txt", encoding="utf-8").read()

########################################################################
def ror(v, n):
  low = v & ((1<<n) - 1)
  return (low << (32-n)) | (v >> n)

n.bit_length() #print bit length of n
if abs(sumdic[key] - x) < 0.00000000000001: #float

print random.randint(12, 20)  #生成的随机数n: 12 <= n <= 20 
gmpy2.next_prime(4)=5

import numpy as np
x = np.linspace(0,1,1500)
y = np.sin(2*np.pi*x*freq)*7
hex(m)[2:].decode('hex')  

import math
math.factorial(3) #3! = 6

########################################################################
from Crypto.Cipher import AES

key = '61323764353962643238316365623464'.decode('hex') #'a27d59bd281ceb4d'
iv = '00000000000000000000000000000000'.decode('hex')
cipher = AES.new(key, AES.MODE_CBC, iv) #AES.MODE_ECB

msg = '36CA216395933344049B6A1CBE9E28851BEDF4986CEDEE09F01FD4777527567251489188A0D4A3412E1AA0F2EF2B3EB6'.decode('hex')
print cipher.decrypt(msg).encode('hex')

#plain = '386330343035363738666331356439616462303332613034656564626331386300000000000000000000000000000000'.decode('hex') #8c0405678fc15d9adb032a04eedbc18c
#print cipher.encrypt(plain).encode('hex')

import zlib
crc = zlib.zrc32('IEND') & 0xffffffff

import bubblepy
bubblepy.BubbleBabble().decode('xevek_duvyk_hunuf_gesuf_dotyf_besif_fusif_nemyk_hexix')

import quopri #quoted-printable
quopri.decodestring('=E5=80=BC=E5=B0=B1')

########################################################################
import requests
r = requests.get(url, cookies={'PHPSESSID': 'abcde'})
r = requests.post(url=url,data=data)
r.status_code
r.content #type:str, jpg/file
if '10' in r.text: #type:unicode

headers = {
    'Refere': 'http://www.baidu.com',
    'User-Agent': 'Mozilla/5.0',
    'Cookie':'x=1'
}
payload = {key1:'value1', key2:'value2'}
reqpost = requests.post("www.xxx.com", data=payload, headers=headers)
print(reqpost.text)
print(reqpost.headers)
print(reqpost.content)

import socket #For windows
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('210.32.4.14', 13373))
data = s.recv(65535)
s.send(ans)

########################################################################
import itertools
fuzzing = "abcdefghijklmnopqrstuvwxyz0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
fuzz = itertools.permutations(string.printable, 5)
string.ascii_letters/string.ascii_lowercase/string.ascii_uppercase/string.digits(0-9)/string.hexdigits(0-9,a-f,A-F)/string.letters(lowercase,uppercase)/string.octdigits(0-7)/string.punctuation
for i in itertools.permutations('ilnke', 5):
    key.append(''.join(i))

for i in itertools.product('ABCD', repeat = 2): #AA AB AC AD...
for i in itertools.permutations('ABCD', 2): #AB AC AD BA BC BD...
for i in itertools.combinations('ABCD', 2): #AB AC AD BC BD CD
for i in itertools.combinations_with_replacement('ABC', 2): #AA AB AC BB BC CC

from itertools import chain
freq_list = [str(i) for i in chain.from_iterable(freq)] #((111, 227),(111, 227)) -> ['111', '227', '111', '227']

########################################################################
import itertools
import progressbar
possibilities = tuple(itertools.product(*possible_values))
for guess in progressbar.ProgressBar(widgets=[progressbar.Counter(), ' ', progressbar.Percentage(), ' ', progressbar.Bar(), ' ', progressbar.ETA()])(possibilities):
        stdout,_ = subprocess.Popen(["./whitehat_crypto400", ''.join(guess)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()

import subprocess
def run(cmd):
  p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  (stdoutdata, stderrdata) = p.communicate()
  return stdoutdata

#matrix#################################################################
from numpy import *
temp = array(temp)
temp = temp.reshape(len(text)/len(public_key), len(public_key))
public_key = numpy.matrix([[3, 1],[2, 1]])
print public_key.T #transpose转置矩阵
[[3 2]
 [1 1]]
print public_key.I #invert逆矩阵
[[ 1. -1.]
 [-2.  3.]]
for i in range(8):
  for j in range(8):
    ch = int(public_key[i, j] + 0.5)

def get_array_from_ida(raw, byte_length): #shift+E extract byte array, then convert to int array
  array = []
  for i in range(0, len(raw), byte_length):
    sum = 0
    for j in range(byte_length):
      sum |= raw[i + j] << (8*j)
    print hex(sum)
    array.append(sum)
  return array

matrix_target = get_array_from_ida(matrix_target_raw, 4)

########################################################################
import getopt
try:
  opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
except getopt.getoptError as err:
  print str(err)

import sys
import os
import time
s = datetime.datetime(2018,9,15,9,42,35)
time.mktime(s.timetuple())
#https://blog.csdn.net/weixin_42591634/article/details/80883028
t = time.strptime("15 Sep 2018 17:42:35", "%d %b %Y %H:%M:%S") #localtimezone!!
time.mktime(t) # time -> epoch_time
for i in sys.path:
    print(i)
print(os.sep, os.path.exists(os.getcwd()), time.strftime('%Y%m%d%H%M%S', time.gmtime(epoch_time)), os.system('echo hello'), sys.stdout.flush())

import platform
import logging
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log') #join with os.sep
print("Logging to", logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")
def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except: #catch all
                log.exception("Attempt %s/%s failed : %s",
                                    attempt,
                                    MAX_ATTEMPTS,
                                    (args, kwargs))
            sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                        MAX_ATTEMPTS,
                        (args, kwargs))
    return wrapped_f
counter = 0
@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    if counter < 2:
     raise ValueError(arg)
if __name__ == '__main__':
    save_to_database("Some bad value")

########################################################################
class Robot:
    _XXX # NOT allow from Robot import *
    __private = 1   # start with __ is private member
    population = 0  # Class variable, similar to static in Java23

    @classmethod
    def how_many(cls):  # Class method, similar to static in Java
        print("We have {:d} robots.".format(cls.population))
    def __init__(self, name):   # Constructor
        self.name = name    # Object variable
        Robot.population += 1
        self.__class__.population +=1

    def __del__(self):  # call before delete, try NOT to use it
        Robot.population -= 1

    def __getitem__(self, item):
        pass    # Reference like x[key]

    def say_hi(self):   # Must specify itself as the first argument
        print('Hello, how are you?')
r = Robot("T1")    # similar to new Person() in Java
r.say_hi()  #Person().say_hi
Robot.how_many()

class ChildRobot(Robot):    # inherit
    def __init__(self, sex):
        Robot.__init__(self, name)  # Must call base class constructor
        self.sex = sex
