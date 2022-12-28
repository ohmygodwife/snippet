#https://zhuanlan.zhihu.com/p/40178190
from PIL import Image, ImageFilter
import os
import pytesseract
from urllib.request import urlretrieve

CHAR_COUNT = 5
url = 'http://www.moguproxy.com/proxy/validateCode/createCode'
TMP_FILE = 'tmp.jpg'
#urlretrieve(url, TMP_FILE)

in_im = Image.open(TMP_FILE)
image = in_im.convert('L') #convert to gray: L = R * 0.299 + G * 0.587+ B * 0.114
image.save('tmpgray.jpg')
#https://blog.csdn.net/FloatDreamed/article/details/79015551
image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image.save('tmpgrayedge.jpg')

width, height = in_im.size
colors = in_im.getcolors(width * height)
sort_colors = sorted(colors, key=lambda x: x[0], reverse=True) #The most color is the background, 1-n is the char

def one_by_one():
  start_map = {}
  for i in range(1, 1+CHAR_COUNT):
    out_im = Image.new('RGB', (width, height))
    start_x = 0
    for x in range(width):
      for y in range(height):
        if in_im.getpixel((x,y)) == sort_colors[i][1]:
          out_im.putpixel((x,y), sort_colors[i][1])
          if not start_x:
            start_x = x
        else:
          out_im.putpixel((x,y), (255, 255, 255))
    
    out_im.save('%d.jpg' % i)
    #https://www.zhihu.com/question/49861652
    #[-psm pagesegmode] pagesegmode values are:
    #3 = Fully automatic page segmentation, but no OSD. (Default) 
    #7 = Treat the image as a single text line.
    #10 = Treat the image as a single character.
    ch = pytesseract.image_to_string(out_im, lang='eng', config='--psm 10')
    print(ch)
#    ch = pytesseract.image_to_string(out_im, lang='mogu', config='--psm 10 --tessdata-dir train')
#    print(ch)
    start_map[start_x] = ch[:1]
  code = ''.join([item[1] for item in sorted(start_map.items(), key=lambda i:i[0])])
  print(code)
  
def all():
  out_im = Image.new('RGB', (width, height))
  for x in range(width):
    for y in range(height):
      pixel = (255, 255, 255)
      for i in range(1, 1+CHAR_COUNT):
        if in_im.getpixel((x,y)) == sort_colors[i][1]:
          pixel = sort_colors[i][1]
          break
      out_im.putpixel((x,y), pixel)
  
#  out_im = out_im.convert('L')
#  out_im = out_im.filter(ImageFilter.EDGE_ENHANCE_MORE)
  code = pytesseract.image_to_string(out_im)
  print(code)

#one_by_one is better than all
one_by_one()
all()
