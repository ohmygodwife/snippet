from PIL import Image
import os
import pytesseract

CHAR_COUNT = 5
RAW_DIR = 'raw'
CHAR_DIR = 'char'

def one_by_one(in_file, out_file):
  in_im = Image.open(in_file)
  width, height = in_im.size
  out_file = out_file[:out_file.rindex('.jpg')]
  print(out_file)
  
  colors = in_im.getcolors(width * height)
  sort_colors = sorted(colors, key=lambda x: x[0], reverse=True) #The most color is the background, 1-n is the char
  
  for i in range(1, 1+CHAR_COUNT):
    out_im = Image.new('RGB', (width, height))
    for x in range(width):
      for y in range(height):
        if in_im.getpixel((x,y)) == sort_colors[i][1]:
          out_im.putpixel((x,y), (0, 0, 0))
        else:
          out_im.putpixel((x,y), (255, 255, 255))
    
    out_im.save('%s-%d.tif' % (out_file, i))

for f in os.listdir(RAW_DIR):
  in_file = os.path.join(RAW_DIR, f)
  out_file = os.path.join(CHAR_DIR, f)
  one_by_one(in_file, out_file)
