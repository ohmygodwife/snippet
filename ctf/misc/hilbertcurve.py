#https://zhuanlan.zhihu.com/p/381863924
#https://blog.csdn.net/m0_49109277/article/details/120387581

import numpy as np
from PIL import Image
from hilbertcurve.hilbertcurve import HilbertCurve

with Image.open('threebody_new.bmp') as img:
    arr = np.asarray(img)
arr = np.vectorize(lambda x: x&1)(arr[:,:,2])

for x1 in range(np.size(arr,0)):
    if sum(arr[x1])>0:
        break
for x2 in reversed(range(np.size(arr,0))):
    if sum(arr[x2])>0:
        break
for y1 in range(np.size(arr,1)):
    if sum(arr[:,y1])>0:
        break
for y2 in reversed(range(np.size(arr,1))):
    if sum(arr[:,y2])>0:
        break

arr = arr[x1:x2+1, y1:y2+1]

hilbert_curve = HilbertCurve(7, 2)

s = ''
for i in range(np.size(arr)):
    [x,y] = hilbert_curve.point_from_distance(i)
    s += str(arr[127-y][x])

with open('output', 'wb') as f:
    f.write(int(s,2).to_bytes(2048, 'big'))