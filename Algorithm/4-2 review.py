def fact(n):
    f = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        f *= i
    return f

print(fact(5))

def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)

print(fact(5))

def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n - 1)

print(sum_rec(100))

def find_max(l: list, n: int):
    if n == 1:
        return l[0]
    max = find_max(l, n - 1)
    if max > l[n - 1]:
        return max
    else:
        return l[n - 1]

lst = [17, 92, 18, 33, 58, 7, 33, 42]   

print(find_max(lst, len(lst)))