from numpy import *

data = [3, 1, 2, 1]

arr = array(data)
arr = arr.reshape(2, 2)
mat = matrix(arr)
mat_invert = mat.I # invert: mat ^ -1
mat_transpose = mat.T # transpose

result = mat_invert * mat
result = result.round() # need to call round to convert to integer first

flag = ''
for i in range(8):
  for j in range(8):
    ch = int(result[i, j])
    flag += chr(ch)

print flag