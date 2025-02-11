def mul_s(a, x):
    n = len(a)
    ans = []
    for i in range(0, n):
        if x == a[i]:
            ans.append(i)
    return ans

def student_num(std, num, c):
    n = len(std)
    for i in range(0, n):
        if c == num[i]:
            return std[i]
    return "?"


lst = [18, 22, 34, 18, 23, 45, 18]
print(mul_s(lst, 18))

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(student_num(stu_name, stu_no, 105))
print(student_num(stu_name, stu_no, 33))