# 4-1
def n_sum_rec(n):
    if n == 1:
        return 1
    return n + n_sum_rec(n - 1)

#4-2
def find_max(a, n):
    if n == 1:
        return a[0]
    mx = find_max(a, n - 1)
    if mx > a[n - 1]:
        return mx
    else:
        return a[n - 1]

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(n_sum_rec(100))
print(find_max(v, len(v)))