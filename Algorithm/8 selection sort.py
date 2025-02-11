def find_min_idx(a: list):
    n = len(a)
    min_idx = 0
    for i in range(0, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

# 새로운 리스트를 만들어서 정리
def sel_sort(a: list):
    result = []
    # list 가 남아있는동안 계속
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

# 주어진 리스트 안에서 정리
def sel_sort_a(a: list):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

# 8-2
def rev_sort(a: list):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]


d = [2, 4, 5, 1, 3]
# print(sel_sort(d))
print(rev_sort(d))
print(d)