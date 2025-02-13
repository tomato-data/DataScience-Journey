student = [1, 2, 3, 4, 5]
student = [i + 100 for i in student ] # student list 안에 있는 숫자를 하나씩 불러오면서 거기에 100을 더한 값을 리스트로 바꿔서 집어넣어라
print(student)

# 학생이름을 길이로 변경
students = ["Joo Hyein", "Park Moosung", "Lee Jehee", "Yoon Sanghyun", "Kim Chaewon", "Choi Junyoung"]
students = [len(i) for i in students]
print(students)

# 학생이름을 대문자로 변경
students = ["Joo Hyein", "Park Moosung", "Lee Jehee", "Yoon Sanghyun", "Kim Chaewon", "Choi Junyoung"]
students = [i.upper() for i in students]
print(students)