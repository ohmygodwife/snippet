# -*- coding: utf-8 -*-

from numpy import *

dic = {chr(i+96): i for i in range(1, 27)}

def decode(text, public_key):

    temp = []
    result = []
    for i in text:
        temp.append(dic.get(i))
    temp = array(temp)
    temp = temp.reshape(len(text)/len(public_key), len(public_key))
    temp =matrix(temp).T
    #print temp
    xx = public_key*temp
    #print xx
    for i in range(len(text)/len(public_key)): #列9
        for j in range(len(public_key)):       #行2
            #print i,j,len(text)/len(public_key),len(public_key)
            result.append(chr(xx[j, i] % 26 + 96))
            print result
    return result

def get_inverse_matrix(public_key):

    public_key_inverse = public_key.I
    temp = public_key_inverse.tolist()
    #print temp
    for i in range(len(public_key)):
        for j in range(len(public_key)):
            temp[i][j] = int(str(temp[i][j]).split('.')[0])
    temp = matrix(temp)
    return temp

if __name__ == '__main__':

    # ciphertext = raw_input("请输入密文: ");
    # ciphertext = list(ciphertext)
    ciphertext = 'dloguszijluswogany'

    # public_key = matrix(array([[1, 2, 3],
    #                            [4, 5, 6],
    #                            [7, 8, 10]]))
    # public_key_inverse = get_inverse_matrix(public_key)
    # print public_key_inverse

    public_key = matrix(array([[1, 2],
                               [0, 1]]))

    public_key_inverse = get_inverse_matrix(public_key)
    #print public_key_inverse
    #print decode(ciphertext, public_key_inverse)
    print "Your flag is :" + "".join(decode(ciphertext, public_key_inverse))