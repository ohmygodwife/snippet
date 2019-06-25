#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{
Title:BeconDecode
Author:Tyler
Type:crypto
Dialog:key1,key2
Detail:培根密码解密
}
'''
def judge_key(ch, key1, key2):
  if ch == key1:
    return 0
  elif ch == key2:
    return 1
  else:
    return None

def judge_case(ch, key1 = None, key2 = None):
  if ch.islower():
    return 0
  elif ch.isupper():
    return 1
  else:
    return None

def add_byte(result, byte):
  for i in range(len(byte)):
    ch = int(byte[i], base=2)
    one = ord('a') + ch
    result[i * 2] += chr(one) #distinct for I/J U/V
    if one >= ord('u'):
      one += 2
    elif one >= ord('j'):
      one += 1
    result[i * 2 + 1] += chr(one) #same for I/J U/V, so ONLY have I/U
    byte[i] = ''

def becon(string, judge, key1 = None, key2 = None):
  result = ['', '', '', '']
  byte = ['', ''] # byte1 = negate byte0
  for ch in string:
    bit = judge(ch, key1, key2)
    if bit is None:
      if len(byte[0]) != 0:
        # could ONLY occur when not a byte start, otherwise return as bad case!
        return ''
      # keep original one
      # could NOT use 'for i in result', change i would not change result[i]
      for i in range(len(result)):
        result[i] += ch
      continue
    byte[0] += str(bit)
    byte[1] += str(bit ^ 1)
    if len(byte[0]) == 5:
      # one byte is found
      add_byte(result, byte)
  return '\n'.join(result)

def main(string, key1 = None, key2 = None):
  if key1 is None or len(key1) == 0:
    return becon(string, judge_case)
  else:
    return becon(string, judge_key, key1, key2)

if __name__ == '__main__':
  print main('haHpY CryPToLOgy')
  print main('BAABB AABAA BAABA BAABB ABAAA BAABB', 'A', 'B')
