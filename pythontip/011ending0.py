L = [32, 5, 5, 5, 5, 0]

def fun(i, x):
  cnt = 0
  while i % x == 0:
    i /= x
    cnt += 1
  return i, cnt

cnt10 = 0
cnt2 = 0
cnt5 = 0
bzero = False
for i in L:
  if i == 0:
    bzero = True
    break
  i, cnt = fun(i, 10)
  cnt10 += cnt
  i, cnt = fun(i, 2)
  cnt2 += cnt
  i, cnt = fun(i, 5)
  cnt5 += cnt
  
if bzero:
  cnt10 = 1
else:
  cnt10 += min(cnt2, cnt5)
print cnt10