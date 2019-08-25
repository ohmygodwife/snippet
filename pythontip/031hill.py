h=[0.9,1.2,1.22,1.1,1.6,0.99]

cnt = 0
start = False
for i in range(len(h) - 1):
  if h[i] < h [i+1]:
    start = True
  if h[i] > h [i+1]:
    if start:
      start = False
      cnt += 1
      
print cnt