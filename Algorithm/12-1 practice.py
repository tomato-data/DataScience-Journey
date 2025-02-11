def binary_sub(a: list, x, s, e):
    if s > e:
        print("s>e")
        return -1
    mid = (s + e) // 2
    print(mid)
    if x == a[mid]:
        print("answer")
        return mid
    elif x > a[mid]:
        print(">")
        return binary_sub(a, x, mid + 1, e)
    else:
        print("<")
        return binary_sub(a, x, s, mid - 1)
    
    return -1

def binary_s(a, x):
    return binary_sub(a, x, 0, len(a) - 1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_s(d, 36))
print(binary_s(d, 50))