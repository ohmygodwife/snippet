#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{
Title:RotateAsciiDecode
Author:Tyler
Type:crypto
Detail:Ascii移位解密
}
'''


def rot(ciphertext):
  plaintext = []
  for i in range(-127, 128):
    plaintext.append(str(i) + ', ')
    for ch in ciphertext:
      v = (ord(ch) + i) & 0x7f
      plaintext.append(chr(v))
    plaintext.append('\n')
  return ''.join(plaintext)

  return plaintext


def main(ciphertext):
  return rot(ciphertext)


if __name__ == '__main__':
  print main('ag2a`f76')