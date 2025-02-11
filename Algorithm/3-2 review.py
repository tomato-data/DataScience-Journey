nl = ['Tom', 'Jerry', 'Mike', 'Tom']

def sn(l: list):
    sn = set()
    n = len(l)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if l[i] == l[j]:
                sn.add(l[i])
    return sn

print(sn(nl))

names = ['Tom', 'Jerry', 'Mike']
def pair(l: list):
    n = len(l)
    result = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            result.add(l[i] + ' - ' + l[j])
    return result

print(pair(names))