#https://mp.weixin.qq.com/s/FGGceMvAZ9iRmIVIufBpBw

import os, zlib
from Crypto.Util.number import *
from PIL import Image
from tqdm import tqdm
import struct

def pngparse(filepath1):
    fr = open(filepath1, 'rb').read()

    chunckid = [b'IHDR', b'PLTE', b'IDAT', b'IEND', b'cHRM', b'gAMA', b'iCCP', b'sBIT', b'sRGB', b'bKGD', b'hIST',
                b'tRNS', b'pHYs', b'sPLT', b'tIME', b'iTXt', b'tEXt', b'zTXt']
    chuncks = []
    i = 4
    while i < len(fr):
        if fr[i:i + 4] in chunckid:
            try:
                datalen, dataname = struct.unpack(">I4s", fr[i - 4:i + 4])
                dataformat = '>I4s' + str(datalen) + 's' + '4s'
                datalen, dataname, data, datacrc = struct.unpack(dataformat, fr[i - 4:i - 4 + 8 + datalen + 4])
                realcrc = zlib.crc32(dataname + data).to_bytes(4, 'big')
                if realcrc != datacrc:
                    datacrc = realcrc
                    print(dataname, 'crc32 fixed')
                # print(datalen,bytes.decode(dataname,encoding='utf-8'),hex(int.from_bytes(datacrc,'big')))
                chuncks.append(fr[i - 4:i - 4 + 8 + datalen] + realcrc)
                i = i + 8 + datalen + 4  # 最少加一，防止出现iend
            except:  # 防止不能解析的结构体中出现png chunckid的关键字，指针直接指向下一个。
                i = i + 1
                continue
        else:
            i = i + 1

    idat = [tmp for tmp in chuncks if tmp[4:8] == b'IDAT']
    blocks = [tmp[8:int.from_bytes(tmp[:4], 'big') + 8] for tmp in chuncks if tmp[4:8] == b'IDAT']
    blocks = b''.join(blocks)  # 组合数据
    data = zlib.decompressobj().decompress(blocks)  # 解码zlib得到像素（含filter）
    width = bytes_to_long(fr[16:20])
    height = bytes_to_long(fr[20:24])
    colorchannel = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[bytes_to_long(fr[25:26])]
    bits = bytes_to_long(fr[24:25])
    perlinebytes = bits * colorchannel * width // 8 + 1  # 每行字节数

    filters = [(data[i]) for i in range(0, len(data), perlinebytes)]

    return fr, width, height, colorchannel, bits, perlinebytes, filters


def parseimg(filepath1):
    img = Image.open(filepath1)
    width = img.size[0]
    height = img.size[1]

    if img.mode == 'RGBA':
        pass
    elif img.mode == 'RGB':
        print('不含alpha通道，需要将图片转换位RGBA')
        img = img.convert('RGBA')
        # img.save('test.png')
    pixel = []
    for h in range(height):
        for w in range(width):
            color = img.getpixel((w, h))
            r = color[0]
            g = color[1]
            b = color[2]
            a = color[3]
            pixel.append((r, g, b, a))
            # pixel=pixel+'\n'
        # fw.write(str(pixel))

    def list_split(items, n):  # 将像素集按照宽度width拆分成n个数组
        return [items[i:i + n] for i in range(0, len(items), n)]

    scanlines = list_split(pixel, width)
    return scanlines


def load_imgs(folder):
    '''
    加载文件夹下的图片
    '''
    imgpath = []
    # img=[]
    for img_path in os.listdir(folder):
        ext = os.path.splitext(img_path)
        # if len(ext) > 1 and is_img(ext[1]):
        if ext[1] == '.png' or ext[1] == '.jpg' or ext[1] == '.bmp':
            filename = folder + '/' + img_path
            imgpath.append(filename)
            # img.append(img_path)

    return imgpath


def num2filter(pathname):
    pathname = pathname[-8:-4]
    b = []
    for i in pathname:
        if i == '1':
            b.append([4, 4, 4, 4, 4])
            b.append([1, 1, 1, 1, 1])
        elif i == '2':
            b.append([4, 1, 4, 4, 4])
            b.append([4, 4, 4, 1, 4])
        elif i == '3':
            b.append([4, 1, 4, 1, 4])
            b.append([4, 4, 4, 4, 4])
        elif i == '4':
            b.append([4, 4, 4, 1, 1])
            b.append([4, 4, 4, 4, 4])
        elif i == '5':
            b.append([4, 4, 4, 1, 4])
            b.append([4, 1, 4, 4, 4])
        elif i == '6':
            b.append([4, 4, 4, 4, 4])
            b.append([4, 1, 4, 4, 4])
        elif i == '7':
            b.append([4, 1, 1, 1, 1])
            b.append([4, 4, 4, 4, 4])
        elif i == '8':
            b.append([4, 4, 4, 4, 4])
            b.append([4, 4, 4, 4, 4])
        elif i == '9':
            b.append([4, 4, 4, 1, 4])
            b.append([4, 4, 4, 4, 4])
        elif i == '0':
            b.append([0, 0, 0, 0, 0])
            b.append([0, 0, 0, 0, 0])
            # print(b)
    # t=[]
    t = ''
    for i in range(0, 5):
        # t.append([x[i] for x in b])
        # t1=[str(x[i]) for x in b]
        for x in b:
            t += str(x[i])

    print(t)

    return t


def filter2num(myfilters):
    myft = [myfilters[i:i + 8] for i in range(0, len(myfilters), 8)]

    b = []
    for i in range(0, 8, 1):
        b.append([int(x[i]) for x in myft])

    c = ''
    for t in range(0, 8, 2):
        if b[t] == [4, 4, 4, 4, 4] and b[t + 1] == [1, 1, 1, 1, 1]:
            c += '1'
        elif b[t] == [4, 1, 4, 4, 4] and b[t + 1] == [4, 4, 4, 1, 4]:
            c += '2'
        elif b[t] == [4, 1, 4, 1, 4] and b[t + 1] == [4, 4, 4, 4, 4]:
            c += '3'
        elif b[t] == [4, 4, 4, 1, 1] and b[t + 1] == [4, 4, 4, 4, 4]:
            c += '4'
        elif b[t] == [4, 4, 4, 1, 4] and b[t + 1] == [4, 1, 4, 4, 4]:
            c += '5'
        elif b[t] == [4, 4, 4, 4, 4] and b[t + 1] == [4, 1, 4, 4, 4]:
            c += '6'
        elif b[t] == [4, 1, 1, 1, 1] and b[t + 1] == [4, 4, 4, 4, 4]:
            c += '7'
        elif b[t] == [4, 4, 4, 4, 4] and b[t + 1] == [4, 4, 4, 4, 4]:
            c += '8'
        elif b[t] == [4, 4, 4, 1, 4] and b[t + 1] == [4, 4, 4, 4, 4]:
            c += '9'
        elif b[t] == [0, 0, 0, 0, 0] and b[t + 1] == [0, 0, 0, 0, 0]:
            c += '0'
        else:
            print('maybe not a number')
    print(c)
    return c


def filter0_none(scanlines, colorchannel, bits, width, tmp, row):
    data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in
            scanlines[row]]
    return b'\x00' + b''.join(data)


def filter1_sub(scanlines, colorchannel, bits, width, tmp, row):
    data = [scanlines[row][0]]
    for tmp in range(1, width): 
        tmp_r = (scanlines[row][tmp][0] - scanlines[row][tmp - 1][0]) & 0xff
        tmp_g = (scanlines[row][tmp][1] - scanlines[row][tmp - 1][1]) & 0xff
        tmp_b = (scanlines[row][tmp][2] - scanlines[row][tmp - 1][2]) & 0xff
        tmp_a = (scanlines[row][tmp][3] - scanlines[row][tmp - 1][3]) & 0xff
        data.append((tmp_r, tmp_g, tmp_b, tmp_a))
    data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in data]
    return b'\x01' + b''.join(data)


def filter2_up(scanlines, colorchannel, bits, width, tmp, row):
    if row == 0:
        data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in
                scanlines[row]]
        return b'\x02' + b''.join(data)
    else:
        data = []
        for tmp in range(0, width):  
            tmp_r = (scanlines[row][tmp][0] - scanlines[row - 1][tmp][0]) & 0xff
            tmp_g = (scanlines[row][tmp][1] - scanlines[row - 1][tmp][1]) & 0xff
            tmp_b = (scanlines[row][tmp][2] - scanlines[row - 1][tmp][2]) & 0xff
            tmp_a = (scanlines[row][tmp][3] - scanlines[row - 1][tmp][3]) & 0xff
            data.append((tmp_r, tmp_g, tmp_b, tmp_a))
        data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in data]
        return b'\x02' + b''.join(data)


def filter3_average(scanlines, colorchannel, bits, width, tmp, row):
    if row == 0:
        data = [scanlines[row][0]]
        for tmp in range(1, width):
            tmp_r = (scanlines[row][tmp][0] - scanlines[row][tmp - 1][0] // 2) & 0xff
            tmp_g = (scanlines[row][tmp][1] - scanlines[row][tmp - 1][1] // 2) & 0xff
            tmp_b = (scanlines[row][tmp][2] - scanlines[row][tmp - 1][2] // 2) & 0xff
            tmp_a = (scanlines[row][tmp][3] - scanlines[row][tmp - 1][3] // 2) & 0xff
            data.append((tmp_r, tmp_g, tmp_b, tmp_a))
        data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in data]
        return b'\x03' + b''.join(data)
    else:
        data = []
        first_r = (scanlines[row][0][0] - scanlines[row - 1][0][0] // 2) & 0xff
        first_g = (scanlines[row][0][1] - scanlines[row - 1][0][1] // 2) & 0xff
        first_b = (scanlines[row][0][2] - scanlines[row - 1][0][2] // 2) & 0xff
        first_a = (scanlines[row][0][3] - scanlines[row - 1][0][3] // 2) & 0xff
        data.append((first_r, first_g, first_b, first_a))

        for tmp in range(1, width):
            tmp_r = (scanlines[row][tmp][0] - (scanlines[row][tmp - 1][0] + scanlines[row - 1][tmp][0]) // 2) & 0xff
            tmp_g = (scanlines[row][tmp][1] - (scanlines[row][tmp - 1][1] + scanlines[row - 1][tmp][1]) // 2) & 0xff
            tmp_b = (scanlines[row][tmp][2] - (scanlines[row][tmp - 1][2] + scanlines[row - 1][tmp][2]) // 2) & 0xff
            tmp_a = (scanlines[row][tmp][3] - (scanlines[row][tmp - 1][3] + scanlines[row - 1][tmp][3]) // 2) & 0xff
            data.append((tmp_r, tmp_g, tmp_b, tmp_a))
        data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in data]
        return b'\x03' + b''.join(data)


def paeth(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        Pr = a
    elif pb <= pc:
        Pr = b
    else:
        Pr = c
    return Pr


def filter4_paeth(scanlines, colorchannel, bits, width, tmp, row):
    if row == 0:
        data = [scanlines[row][0]]
        for tmp in range(1, width):  # 注意负数要用反码，和ff与一下即可
            tmp_r = (scanlines[row][tmp][0] - scanlines[row][tmp - 1][0]) & 0xff
            tmp_g = (scanlines[row][tmp][1] - scanlines[row][tmp - 1][1]) & 0xff
            tmp_b = (scanlines[row][tmp][2] - scanlines[row][tmp - 1][2]) & 0xff
            tmp_a = (scanlines[row][tmp][3] - scanlines[row][tmp - 1][3]) & 0xff
            data.append((tmp_r, tmp_g, tmp_b, tmp_a))
        data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in data]
        return b'\x04' + b''.join(data)
    else:
        data = []
        first_r = (scanlines[row][0][0] - scanlines[row - 1][0][0]) & 0xff
        first_g = (scanlines[row][0][1] - scanlines[row - 1][0][1]) & 0xff
        first_b = (scanlines[row][0][2] - scanlines[row - 1][0][2]) & 0xff
        first_a = (scanlines[row][0][3] - scanlines[row - 1][0][3]) & 0xff
        data.append((first_r, first_g, first_b, first_a))

        for tmp in range(1, width):
            tmp_r = (scanlines[row][tmp][0] - paeth(scanlines[row][tmp - 1][0], scanlines[row - 1][tmp][0],
                                                    scanlines[row - 1][tmp - 1][0])) & 0xff
            tmp_g = (scanlines[row][tmp][1] - paeth(scanlines[row][tmp - 1][1], scanlines[row - 1][tmp][1],
                                                    scanlines[row - 1][tmp - 1][1])) & 0xff
            tmp_b = (scanlines[row][tmp][2] - paeth(scanlines[row][tmp - 1][2], scanlines[row - 1][tmp][2],
                                                    scanlines[row - 1][tmp - 1][2])) & 0xff
            tmp_a = (scanlines[row][tmp][3] - paeth(scanlines[row][tmp - 1][3], scanlines[row - 1][tmp][3],
                                                    scanlines[row - 1][tmp - 1][3])) & 0xff
            data.append((tmp_r, tmp_g, tmp_b, tmp_a))
        data = [long_to_bytes(i[0]) + long_to_bytes(i[1]) + long_to_bytes(i[2]) + long_to_bytes(i[3]) for i in data]

        return b'\x04' + b''.join(data)



if __name__ == "__main__":
    im1 = Image.new('RGBA', (32 * 160, 18 * 160), 'white')

    path = r'./img/'
    pathnames = load_imgs(path)
    for filepath1 in tqdm(pathnames):
        with open(filepath1, 'rb')as f:
            fr = f.read()
        x = int.from_bytes(fr[6:8], 'little')
        y = int.from_bytes(fr[8:10], 'little')
        im2 = Image.open(filepath1)
        im1.paste(im2, (x * 32, y * 18))
        pass
    im1.show()
    im1.save('flag.png')
    pass