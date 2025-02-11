# O(n)

def weigh(a, b, c, d):
    fake = 29
    if a <= fake <= b:
        return -1
    if c <= fake <= d:
        return 1
    return 0

def find_fakecoin(start, end):
    for i in range(start + 1, end + 1):
        result = weigh(start, start, i, i)
        if result == -1:
            return start
        elif result == 1:
            return i
    return -1

n = 100
print(find_fakecoin(0, n - 1))