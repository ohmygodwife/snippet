#Omni Crypto, pwn2win-2020, https://furutsuki.hatenablog.com/entry/2020/06/01/023111

def sqrt_power_of_2_mod(a, n):
    """find x^2 = a mod 2^n""" 
    assert a % 8 == 1

    res = []
    for x in [1, 3]:
        for k in range(3, n):
            i = ((x*x - a) // pow(2, k)) % 2
            x = x + i * pow(2, k-1)

        res.append(x)
        res.append(2**n - x)
    return res