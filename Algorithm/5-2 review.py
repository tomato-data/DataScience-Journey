def gcd(a: int, b: int):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        else:
            i -= 1

def gcd_rec(a: int, b: int):
    if b == 0:
        return a
    return gcd_rec(b, a % b)

print(gcd_rec(60, 24))