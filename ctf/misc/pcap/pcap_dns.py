#stealer, dasctf-202108, https://blog.csdn.net/qq_42815161/article/details/120010131
#https://ctf-wiki.org/misc/traffic/protocols/dns/
#D:\ctf\tools\web\Wireshark\tshark.exe  -r ..\misc_dump.pcapng -T fields -e dns.qry.name -Y "ip.src==172.27.221.13"> hex

import re

flag = ''
with open('hex', 'r') as f:
    for line in f:
        if len(line) <= 100: #filter some noise, like: vortex.data.microsoft.com
            continue
        line = line[:-(len('ctf.com.cn\n'))]
        line = line.replace(r'-.', '')
        line = line.replace(r'*', r'+')
        flag += line
#        print line
#        exit()

with open('flag.png', 'wb') as f:
    f.write(flag.decode('base64'))
