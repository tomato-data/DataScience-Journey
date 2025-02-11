# O(n^2)

def same_name(l):
    n = len(l)
    sn = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if l[i] == l[j]:
                sn.add(l[i])
    return sn

name = ["Tom", "Jerry", "Mike", "Tom"]
print(same_name(name))

# range(n, n)은 작동을 하나 안하나