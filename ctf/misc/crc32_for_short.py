# -*- coding: utf-8 -*-
#usage: python crc32_for_short.py 0xa28e7734 -l 2

import argparse
import string
import itertools
import binascii

TABLE = string.ascii_letters + string.digits + '{}_-'#printable/ascii_lowercase/ascii_uppercase/hexdigits/digits

def calc(args):
  target = int(args.target, 0) & 0xffffffff
  for i in itertools.product(TABLE, repeat = args.length):
    src = ''.join(i)
    crc = binascii.crc32(src) & 0xffffffff
    if crc == target:
      print src

def parse_args():
  parser = argparse.ArgumentParser()
  parser.description='please enter target crc32 and source length'
  parser.add_argument("target", help="target crc32 value, in dec or hex", type=str)
  parser.add_argument("-l", "--length", help="source length", type=int, default="2")
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  args = parse_args()
  calc(args)