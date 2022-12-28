#guess_game, wdb-2020-3rd, http://igml.top/2020/05/18
def get_mask(stream):
    dim = len(stream) / 2
    left, right = stream[:dim], stream[dim:]
    magic = [map(int, list(right[:i][::-1] + left[:(dim - i)])) for i in range(dim)] # generate matrix according to lfsr, normally is left shift, here is right shift!!!
    cipher = map(int, list(right))
    print len(cipher)
    assert len(cipher) == dim
    # Gauss-Elimination
    for j in range(dim):
        for i in range(j, dim):
            if magic[i][j] == 1:
                magic[i], magic[j] = magic[j], magic[i]
                cipher[i], cipher[j] = cipher[j], cipher[i]
                break
        for i in range(dim):
            if magic[i][j] == 1 and i != j:
                for k in range(dim):
                    magic[i][k] ^= magic[j][k]
                cipher[i] ^= cipher[j]
    return int(''.join(map(str, cipher)), 2)
    
print get_mask('01010111111110101011')