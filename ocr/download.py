from urllib.request import urlretrieve
import os

os.chdir('raw')
url = 'http://www.moguproxy.com/proxy/validateCode/createCode'

COUNT = 100
for i in range(COUNT):
  urlretrieve(url, '%.4d.jpg' % i)