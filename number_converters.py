
from string import ascii_lowercase

# Get characters into `a` and `f` range.
HEX_CHARS = ascii_lowercase[:6]

def intTo(n,base):
    if n < base: return str(n % base)

    return str(intTo((n // base), base)) + " " + str(n % base)


def intToBinary(n): return intTo(n,2)


def intToHex(n):

    digits_values = {}
    for i in range(16):
        if i < 10:
            digits_values[i] = str(i)
        else:
            digits_values[i] = HEX_CHARS[i - 10]

    bits = intTo(n,16)
    hex_res = ''

    for bit in bits.split():
        hex_res += digits_values[int(bit)]

    return hex_res

def hex_color(porcentage)-> str:
    """
    Given `red, green, blue and alpha(optional)` as a tuble of integers ranging from 0 to 100.
    Returns the hex color representation as a string.
    """

    if len(porcentage) > 4:
        raise Exception("Too Many values! At most 4 (red, green, blue, alpha) values as an iterable.")

    if type(porcentage) != int:
        for i in range(len(porcentage)):
            if porcentage[i] > 100:
                porcentage[i] = 100
                
        values = list(map(lambda p: (p * 255 // 100), porcentage))
    
    elif type(porcentage) == int:
        values = list([porcentage * 255 // 100]*3) if porcentage <= 100 else list([255]*3)

    hex_v = ' '.join(list(map(intToHex,values)))
    for i in hex_v.split():
        if i == '0':
            hex_v += '0'

    return '#'+''.join(hex_v.replace(' ',''))


print(hex_color((50,20,20)))