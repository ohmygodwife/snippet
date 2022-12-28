#python3
#https://learnblockchain.cn/article/1520

def square_root_of_quadratic_residue(n, modulo):
    """Square root of quadratic residue
    
    Solve the square root of quadratic residue using Cipolla's algorithm with Legendre symbol
    Returns:
        int -- if n is a quadratic residue,
                   return x, such that x^{2} = n (mod modulo)
               otherwise, return -1
    """
    if modulo == 2:
        return 1
    if n % modulo == 0:
        return 0
    Legendre = lambda n: pow(n, modulo - 1 >> 1, modulo)
    if Legendre(n) == modulo - 1:
        return -1
    t = 0
    while Legendre(t ** 2 - n) != modulo - 1:
        t += 1
    w = (t ** 2 - n) % modulo
    return (generate_quadratic_field(w, modulo)(t, 1) ** (modulo + 1 >> 1)).x
   
def generate_quadratic_field(d, modulo=0):
    """Generate quadratic field number class
    
    Returns:
        class -- quadratic field number class
    """
    assert(isinstance(modulo, int) and modulo >= 0)
    
    class QuadraticFieldNumber:
        def __init__(self, x, y):
             self.x = x % modulo
             self.y = y % modulo

        def __mul__(self, another):
            x = self.x * another.x + d * self.y * another.y
            y = self.x * another.y + self.y * another.x
            return self.__class__(x, y)

        def __pow__(self, exponent):
            result = self.__class__(1, 0)
            if exponent:
                temporary = self.__class__(self.x, self.y)
                while exponent:
                    if exponent & 1:
                        result *= temporary
                    temporary *= temporary
                    exponent >>= 1
            return result

        def __str__(self):
            return '({}, {} \\sqrt({}))'.format(self.x, self.y, d)

    return QuadraticFieldNumber

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161
x = square_root_of_quadratic_residue(a, p)
print(x)
print(pow(x,2,p) - a)
#x^2 = (p-x)^2 = n mod p