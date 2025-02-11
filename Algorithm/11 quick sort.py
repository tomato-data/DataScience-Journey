def quick_sort(a: list):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort(g1) + [pivot] + quick_sort(g2)

def quick_sort_sub(a: list, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
            print(a)
    a[i], a[end] = a[end], a[i]

    quick_sort_sub(a, start, i - 1)
    quick_sort_sub(a, i + 1, end)

def quick_sort_a(a):
    quick_sort_sub(a, 0, len(a) - 1)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort_a(d)
print(d)