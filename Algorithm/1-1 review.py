def power_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s

print(power_sum(10))

