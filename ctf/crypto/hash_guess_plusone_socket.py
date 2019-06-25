import hashlib
import socket
import string
import random
import time
import sys
import math

def _recv(x):
    global s
    r=s.recv(x)
    sys.stdout.write(r)
    return r

def recv(x,y='wxh'):
    global s
    res=''
    while True:
        u=_recv(1024)
        res+=u
        if res.find(x)!=-1 or res.find(y)!=-1:return res

def send(x):
    global s
    s.send(x)

def hash(s,ht):
    if ht=='sha256':return hashlib.sha256(s).hexdigest()
    if ht=='sha224':return hashlib.sha224(s).hexdigest()
    if ht=='sha384':return hashlib.sha384(s).hexdigest()
    if ht=='sha512':return hashlib.sha512(s).hexdigest()
    if ht=='sha1':return hashlib.sha1(s).hexdigest()
    if ht=='md5':return hashlib.md5(s).hexdigest()

def findcoll(ht,v):
    rs=0
    while hash(str(rs),ht)[-6:]!=v:
        rs+=1
        if rs%100000==0:print rs
    return str(rs)

print findcoll('sha256','06e593')
exit()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('106.75.73.28',20000))

t=recv('such that')
t=t[t.find('such that')+len('such that '):]
ht=t[:t.find('(X)')]
t=t[t.find(' = ')+3:]
v=t[:6]
print ht,v


print rs
send(str(rs)+'\n')

recv('wxh')
