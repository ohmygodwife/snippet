'''https://blog.csdn.net/Herishwater/article/details/94546608
'''
L=[-2,1,-3,4,-1,2,1,-5,4]

for i in range(2, len(L)):
  L[i] = max(max(L[0:i - 1]), 0) + L[i]
  
print L
print max(L)
