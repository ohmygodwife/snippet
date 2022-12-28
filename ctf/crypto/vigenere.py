#dump_mem, xiangshan-2022, https://blog.csdn.net/zerorzeror/article/details/127604534
#https://ask.csdn.net/questions/7821627
def vigenere_encryption(text,key):
    cipher_text = ""
    key = key.upper()
    i = 0
    for w in text:
        i %= len(key)
        if w.isalpha():
            a = ord(w.upper())+ord(key[i])-ord("Z")-1
            if a<ord("A"): a += 26
            a = chr(a)
            if w.islower(): a = a.lower()
            cipher_text += a
            i += 1
        else:
            cipher_text += w
    return cipher_text
 
def vigenere_decrypt(text,key):
    plaintext = ""
    key = key.upper()
    i = 0
    for w in text:
        i %= len(key)
        if w.isalpha():
            a = ord(w.upper())+ord("Z")-ord(key[i])+1
            if a>ord("Z"): a -= 26
            a = chr(a)
            if w.islower(): a = a.lower()
            plaintext += a
            i += 1
        else:
            plaintext += w
    return plaintext

import base64  
cipher = 'ISTMJ1FUvqS4NWGxAqL2MKKfBHWdMnYdMHV5FUIrRHy3Equ2MsT5tE=='
pwfile = 'Password.txt'
with open(pwfile, 'r') as f:
    while True:
        key = f.readline().strip()
        if not key:
            break
        plain = vigenere_decrypt(cipher, key)
        try:
            plain = base64.b64decode(plain).decode()
            if plain.isprintable():
                print(plain)
        except Exception:
            pass


#print(vigenere_decrypt('ISTMJ1FUvqS4NWGxAqL2MKKfBHWdMnYdMHV5FUIrRHy3Equ2MsT5tE==', 'roottoor'))