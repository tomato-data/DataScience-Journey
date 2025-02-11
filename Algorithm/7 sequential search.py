# def s_search(l, f):
#     ans = []
#     for i in f:
#         if i in l:
#             ans.append(l.index(i))
#         else:
#             ans.append(-1)
#     return ans

# lst = [17, 92, 18, 33, 58, 7, 33, 42]
# f = [18, 33, 900]

# print(s_search(lst, f))

def s_search(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(s_search(v, 18))
print(s_search(v, 33))
print(s_search(v, 900))