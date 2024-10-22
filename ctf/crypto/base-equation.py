#numpy is beter than z3
import numpy as np
coefficient = [2, 3, 3, 4]
result = [18, 25]
len1 = len(coefficient)
len2 = len(result)

#https://numpy.org/devdocs/reference/generated/numpy.linalg.solve.html
def doNpLinalg():
  arr1 = np.array(coefficient)
  arr1 = arr1.reshape(len2, len1/len2)
  arr2 = np.array(result)
  x = np.linalg.solve(arr1,arr2)
  print x
  x = x.round()
  flag = ''
  for i in x:
    ch = int(i)
    flag += chr(ch)
  print flag

doNpLinalg()

def doNpMatrix():
  arr1 = np.array(coefficient)
  arr1 = arr1.reshape(len2, len1/len2)
  mat1 = np.matrix(arr1)

  arr2 = np.array(result)
  arr2 = arr2.reshape(len2, 1) #arr2.reshape(-1, 1)
  mat2 = np.matrix(arr2)

  mat3 = mat1.I * mat2
  mat3 = mat3.round()
  print mat3
  flag = ''
  for i in range(len1/len2):
    ch = int(mat3[i, 0])
    flag += chr(ch)
  print flag

doNpMatrix()

def doZ3():
  from z3 import *
  s = Solver()
  v1,v2,v3,v4,v5,v6,v7,v8 = Ints('v1 v2 v3 v4 v5 v6 v7 v8')
  s.add(331 * v7 + 317 * v6 + 313 * v5 + 311 * v4 + 307 * v3 + 293 * v2 + 283 * v1 + 337 * v8 - 225643 == 0)
  s.add(509 * v7 + 503 * v6 + 499 * v5 + 491 * v4 + 487 * v3 + 479 * v2 + 467 * v1 + 521 * v8 - 356507 == 0)
  s.add(587 * v7 + 577 * v6 + 571 * v5 + 569 * v4 + 563 * v3 + 557 * v2 + 547 * v1 + 593 * v8 - 410769 == 0)
  s.add(643 * v7 + 641 * v6 + 631 * v5 + 619 * v4 + 617 * v3 + 613 * v2 + 607 * v1 + 647 * v8 - 450797 == 0)
  s.add(773 * v7 + 769 * v6 + 761 * v5 + 757 * v4 + 751 * v3 + 743 * v2 + 739 * v1 + 787 * v8 - 546531 == 0)
  s.add(853 * v7 + 839 * v6 + 829 * v5 + 827 * v4 + 823 * v3 + 821 * v2 + 811 * v1 + 857 * v8 - 598393 == 0)
  s.add(919 * v7 + 911 * v6 + 907 * v5 + 887 * v4 + 883 * v3 + 881 * v2 + 877 * v1 + 929 * v8 - 646297 == 0)
  s.add(1319 * v7 + 1307 * v6 + 1303 * v5 + 1301 * v4 + 1297 * v3 + 1291 * v2 + 1289 * v1 + 1321 * v8 - 935881 == 0)
  if (s.check() == sat):
    print s.model()
  else:
    print "unsat"

doZ3()

def doSym():
  from sympy import *
  v1=Symbol('v1')
  v2=Symbol('v2')
  v3=Symbol('v3')
  v4=Symbol('v4')
  v5=Symbol('v5')
  v6=Symbol('v6')
  v7=Symbol('v7')
  v8=Symbol('v8')
  print solve([331 * v7 + 317 * v6 + 313 * v5 + 311 * v4 + 307 * v3 + 293 * v2 + 283 * v1 + 337 * v8 - 225643 , 509 * v7 + 503 * v6 + 499 * v5 + 491 * v4 + 487 * v3 + 479 * v2 + 467 * v1 + 521 * v8 - 356507, 587 * v7 + 577 * v6 + 571 * v5 + 569 * v4 + 563 * v3 + 557 * v2 + 547 * v1 + 593 * v8 - 410769, 643 * v7 + 641 * v6 + 631 * v5 + 619 * v4 + 617 * v3 + 613 * v2 + 607 * v1 + 647 * v8 - 450797, 773 * v7 + 769 * v6 + 761 * v5 + 757 * v4 + 751 * v3 + 743 * v2 + 739 * v1 + 787 * v8 - 546531, 853 * v7 + 839 * v6 + 829 * v5 + 827 * v4 + 823 * v3 + 821 * v2 + 811 * v1 + 857 * v8 - 598393, 919 * v7 + 911 * v6 + 907 * v5 + 887 * v4 + 883 * v3 + 881 * v2 + 877 * v1 + 929 * v8 - 646297, 1319 * v7 + 1307 * v6 + 1303 * v5 + 1301 * v4 + 1297 * v3 + 1291 * v2 + 1289 * v1 + 1321 * v8 - 935881],[v1,v2, v3, v4, v5, v6, v7, v8])
  
doSym()