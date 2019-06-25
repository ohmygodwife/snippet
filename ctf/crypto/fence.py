#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{
Title:FenceDecode
Author:Tyler
Type:crypto
Detail:栅栏密码解密
}
'''


def fence_step(ciphertext, step):
  length = len(ciphertext)
  plaintext = [ciphertext[0]] * length
  j = i = 0
  for ch in ciphertext[1:]:
    j += step
    if j >= length:
      i += 1
      j = i
    plaintext[j] = ch
  return ''.join(plaintext)

def fence(ciphertext):
  plaintext = []
  for step in range(2, len(ciphertext)):
    plaintext.append(fence_step(ciphertext, step))
    plaintext.append('\n')
  return ''.join(plaintext)

  return plaintext


def main(ciphertext):
  return fence(ciphertext)


if __name__ == '__main__':
  print main('fc_nt}lritiaysengp_rg{tis')

#wrong: fc_nt}lritiaysengp_rg{tis
#correct: fc_ntlritiaysengp_rg{tis}