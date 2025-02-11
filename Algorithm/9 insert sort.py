def find_ins_idx(r: list, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

# 새로운 리스트에 정리
def ins_sort(a: list):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result  

# list 안에서 직접 위치를 바꿔 정렬하는 프로그램

def ins_sort_a(a: list):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            print(a)
        a[j + 1] = key

# 9-2
def rev_sort(a: list):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key



d = [2, 4, 5, 1, 3]
# print(ins_sort(d))
ins_sort_a(d)
print(d)