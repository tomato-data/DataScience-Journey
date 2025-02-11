def find_max(a: list):
    max_val = 0
    for i in a:
        if max_val < i:
            max_val = i
    return a.index(max_val)

def find_min(a: list):
    min_val = 0
    for i in a:
        if min_val == 0:
            min_val = i
        elif min_val > i:
            min_val = i
    return min_val

lst = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_min(lst))
print(find_max(lst))