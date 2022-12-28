#python3
digits = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
units = {'佰': 100.0, '拾':10.0, '元': 1.0, '角': 0.1, '分': 0.01}

def parse(s):
  cnt = 0.0
  i = 0
  while i < len(s):
    if s[i] == '整' or s[i] == '元':
      i += 1
      continue
    d = digits.index(s[i])
    i += 1
    u = 1.0
    if i < len(s):
      if s[i] in units:
        u = units[s[i]]
        i += 1
    cnt += d * u
  return cnt

cnt = 0.0
with open('misc_account.csv', 'r') as f:
  for line in f:
    arr = line.strip().split(',')
    cnt += parse(arr[0]) * parse(arr[1])
    
print(cnt)