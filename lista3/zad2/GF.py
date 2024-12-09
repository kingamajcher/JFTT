def to_GF(a: int, G: int) -> int:
    return (((a % G) + G) % G)
    
def euclid_algorithm(a: int, b: int) -> (int, int, int):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = euclid_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y
    
def inverse_GF(a: int, G: int) -> int:
    _, x, _ = euclid_algorithm(a, G,)
    return to_GF(x, G)

def divide_GF(a: int, b: int, G: int) -> int:
    inverse = inverse_GF(b, G)
    return int((a * inverse) % G)

def power_GF(a: int, power: int, G: int)  -> int:
    result = a
    if (power == 0):
        return 1 
    elif (power == 1):
        return a
    for i in range(2, power+1):
        result = (result * a) % G
        
    return result
