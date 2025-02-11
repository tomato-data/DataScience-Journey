def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

def rec_factorial(n):
    # 종료조건
    if n <= 1:
        return 1
    return n * rec_factorial(n - 1)

print(rec_factorial(10))
