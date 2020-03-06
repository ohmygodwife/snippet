'''
$gnuplot
gnuplot>plot '1.txt' #file with lines of points
'''

#https://www.cnblogs.com/zhizhan/p/5615947.html
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from PIL import Image

#point
x = [11422,11360,11312,11274,11233,11196,11160,11129,11098,11038]
y = [123,120,115,110,105,100,95,90,85,80]

#plt.scatter(x, y) #draw points
plt.plot(x, y, 'r-o') #draw points and line. - for line, o for point, * for star
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

#forward,backward,turn left/right, car:redhat-2019,https://www.cnblogs.com/basstorm/p/11885798.html
import turtle

turtle.left(90)
for i in range(len(A)):
  if En[i] == 1:
    if A[i] == 1 and B[i] == 1:
      turtle.forward(5)
    if A[i] == 0 and B[i] == 0:
      turtle.backward(5)
    if A[i] == 1 and B[i] == 0:
      turtle.right(90)
    if A[i] == 0 and B[i] == 1:
      turtle.left(90)

turtle.mainloop()

#rgb
x = 887 
y = 111 
im = Image.new('RGB',(x,y))
file = open('ce.txt')
for i in xrange(0,x):
  for j in xrange(0,y):
    rgb = c = file.readline().split(",")
    im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))

im.show()

#ONLY support png file!
png = mpimg.imread('D:/ctf/ichunqiu/2018cdgcrace/loli/outfile/png/00006777.png')
height,width,depth = png.shape
print height, width, depth
for i in range(height):
  for j in range(width):
    for k in range(depth):
      print png[i][j][k]


#https://www.cnblogs.com/chimeiwangliang/p/7130434.html
# jpg
im = Image.open('D:/ctf/ichunqiu/sheng2/kaixin.jpg')
print im.height, im.width, im.height*im.width
print im.mode
seq = list(im.getdata())
print len(seq)
for i in range(im.height):
  for j in range(im.width):
    for k in range(3): #RGB
      print seq[i * im.height + j][k]
#im.convert("1") #