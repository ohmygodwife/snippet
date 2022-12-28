#cmcc\200421\WEB\web-Audit
import re

#dvwa.flag_is_here%20ORDER%20BY%20flag%20LIMIT%200%2C1%29%2C22%2C1%29%29%3E125%20AND%20%27RCKM%27%3D%27RCKM&Submit=Submit HTTP/1.1" 404 5476

def get_char(last_char, last_length):
  v = int(last_char)
  if last_length == '1765': #True
   v += 1
  return chr(v)

with open('access.log', 'r') as f:
  last_index = '1'
  last_char = ''
  last_length = ''
  flag = ''
  for line in f:
    m = re.search('dvwa.flag_is_here%20ORDER%20BY%20flag%20LIMIT%200%2C1%29%2C(\d+)%2C1%29%29%3E(\d+)%20AND%20%27RCKM%27%3D%27RCKM&Submit=Submit HTTP/1.1" 404 (\d+)', line)
    if m:
      if m.group(1) != last_index:
        flag += get_char(last_char, last_length)
      last_index = m.group(1)
      last_char = m.group(2)
      last_length = m.group(3)
      print last_index, last_char, last_length

flag += get_char(last_char, last_length)
print flag