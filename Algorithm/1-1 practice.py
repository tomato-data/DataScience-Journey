def power_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s

print(power_sum(10))

def power_sum2(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

print(power_sum2(10))