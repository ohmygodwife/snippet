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
  for i in range(1, 128):
    for ch in ciphertext:
      v = (ord(ch) + i) & 0x7f
      plaintext.append(chr(v))
    plaintext.append('\n')
  return ''.join(plaintext)

  return plaintext


def main(ciphertext):
  return rot(ciphertext)


if __name__ == '__main__':
  print main('PD4~idqQC|WjHloX>)UPb8~ZFb8laGczAeteE')