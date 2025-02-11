def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

# Euclidean Algorithm

def rec_gcd(a, b):
    if b == 0:
        return a
    return rec_gcd(b, a % b)


print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))

print(rec_gcd(1, 5))
print(rec_gcd(3, 6))
print(rec_gcd(60, 24))
print(rec_gcd(81, 27))