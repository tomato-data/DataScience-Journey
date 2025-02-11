# 풀기 전 만들어 보기

# def palindrome(a: str):
#     b = []
#     c = []
#     n = len(a)
#     for i in a:
#         b.append(i)
#         c.append(i)
#     for j in range(1):
#         comp_b = b.pop(0)
#         comp_c = b.pop()
#         if comp_b == comp_c:
#             continue
#         else:
#             return "no!"
#     return "Yes!"

def palindrome(s: str):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    
    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))