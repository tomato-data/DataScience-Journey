def pair(l):
    n = len(l)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(l[i], "-", l[j])

name = ["Tom", "Jerry", "Mike"]
print(pair(name))