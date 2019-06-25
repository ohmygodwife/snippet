#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{
Title:Substitute
Author:Tyler
Type:crypto
Dialog:src,dst
Detail:简单替换
}
'''
import string

def substitute(ciphertext, src, dst):
  code = {}
  for i in range(0, len(src)):
    code[src[i]] = dst[i]
  plain = []
  for ch in ciphertext:
    if code.has_key(ch):
      plain.append(code[ch])
    else:
      plain.append(ch)
  return "".join(plain)


def main(ciphertext, src, dst):
  table = string.maketrans(src, dst)
  return ciphertext.translate(table)

  return substitute(ciphertext, src, dst)


if __name__ == '__main__':
  print main('1adcab2', 'abcd', 'efgh')