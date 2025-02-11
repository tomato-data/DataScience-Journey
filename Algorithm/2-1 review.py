lst = [17, 92, 18, 33, 58, 7, 33, 42]

def find_max(l: list):
    mx = 0
    for i in l:
        if mx < i:
            mx = i
    return mx

print(find_max(lst))

def max_idx(l:list):
    mx = 0
    for i in l:
        if mx < i:
            mx = i
    return l.index(mx)

print(max_idx(lst))

def find_min(l: list):
    mn = 99
    for i in l:
        if mn > i:
            mn = i
    return mn

print(find_min(lst))