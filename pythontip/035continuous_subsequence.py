L=[2,-3,3,50]

sum = 0
max = L[0]
for i in L:
  sum += i
  if sum > max:
      max = sum
  elif sum < 0:
    sum = 0
    
print max