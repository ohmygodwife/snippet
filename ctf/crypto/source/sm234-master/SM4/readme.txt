D:\ctf\tools\encrypt\sm234-master\SM4>sm4.exe
Usage: sm4 [-e(encrypt)|-d(decrypt)|-c(cbc_encrypt)|-b(cdc_decrypt]

D:\ctf\tools\encrypt\sm234-master\SM4>sm4.exe -d

input ciphertext(in hex):c7bca4f4ac186239cad1cb2d797c14c3224bba522954016232d3c8e18a085c84f68d31ab1151d58560f96a3c05c6b329

input 128-bit secret key(in hex):DA98F1DA312AB753A5703A0BFD290DD6

plainnum = 666c61677b65343433353334312d343031612d346263342d393663312d6561646631393531643930347dffffffffffff
plaintext = flag{e4435341-401a-4bc4-96c1-eadf1951d904}

D:\ctf\tools\encrypt\sm234-master\SM4>sm4.exe -e

input plaintext(in hex):666c61677b65343433353334312d343031612d346263342d393663312d6561646631393531643930347dffffffffffff

input 128-bit secret key(in hex):DA98F1DA312AB753A5703A0BFD290DD6

ciphertext = c7bca4f4ac186239cad1cb2d797c14c3224bba522954016232d3c8e18a085c84f68d31ab1151d58560f96a3c05c6b329

D:\ctf\tools\encrypt\sm234-master\SM4>sm4.exe -c

input 128-bit initial value:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

input plaintext(in hex):666c61677b65343433353334312d343031612d346263342d393663312d6561646631393531643930347dffffffffffff

input 128-bit secret key(in hex):DA98F1DA312AB753A5703A0BFD290DD6

ciphertext = 8aad39dc8d8dd1ac44c1802fe8345ec68ac50556636b4d10bda8c525d6e12dff52fbb9fd4a68bd570c8dcd67aad3fdee

D:\ctf\tools\encrypt\sm234-master\SM4>sm4.exe -b

input 128-bit initial value:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

input ciphertext(in hex):8aad39dc8d8dd1ac44c1802fe8345ec68ac50556636b4d10bda8c525d6e12dff52fbb9fd4a68bd570c8dcd67aad3fdee

input 128-bit secret key(in hex):DA98F1DA312AB753A5703A0BFD290DD6

plainnum = 666c61677b65343433353334312d343031612d346263342d393663312d6561646631393531643930347dffffffffffff
plaintext = flag{e4435341-401a-4bc4-96c1-eadf1951d904}