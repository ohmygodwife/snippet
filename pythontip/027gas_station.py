n = 9
limit = [1, 1, 1, -2, 1, -3, 4, 1, -10]
cost = [0, 0, 0, 0, 0, 0, 0, 0, 0]

left = map(lambda (a,b):a-b,zip(limit, cost))
start = 0
cur = 0
back = 0

for i in range(n):
  cur += left[i]
  while cur < 0 and start <= i:
      cur -= left[start]
      back += left[start]
      start += 1
    
if cur + back >= 0:
  print start
else:
  print -1