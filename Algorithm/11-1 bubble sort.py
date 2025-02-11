def smthing_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                print(a)
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True  
        if changed == False:
            return
    
def bubble_sort(a):
    n = len(a)
    i = 1
    while i < n:
        if a[i] < a[i - 1]:
            print('changing: ', a[i - 1], a[i])
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
            print(a)
            if i < 1:
                i = 1
        else:
            i += 1

def bubble_sort_a(a):
    n = len(a)
    i = 1
    ia = 1
    while i < n:
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
            print(a)
            if i < 1:
                i = 1
        else:
            i += 1
            ia += 1

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)