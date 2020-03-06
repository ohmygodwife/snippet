import socket,sys
import random
import math
import time
import threading

ADDR = ('127.0.0.1',10086)
BUFSIZE = 1024

def link(i):
  sock = socket.socket()
  try:
    sock.connect(ADDR)
    print(i, 'have connected with server')
    low = 0
    high = pow(2, 128)
    while low <= high:
      mid = (low+high)/2
      sock.send(str(mid) + '\n')
      res = sock.recv(BUFSIZE)
      if res == 'big':
        high = mid - 1
      elif res == 'small':
        low = mid + 1
      else:
        print mid
        break
  except Exception:
    print('error')
  sock.close()
  sys.exit()

for i in range(1):
  thread = threading.Thread(target=link,args=(i,))
  thread.start()