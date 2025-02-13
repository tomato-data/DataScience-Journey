absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue # continue를 만나면 밑에 문장 실행하는게 아니라 다음 반복으로 넘어감
    elif student in no_book:
        print("today's class ends here, {0}, meet me at the office." .format(student))
        break # 뒤에 반복문이 있던 없던 끝내버림
    print("{0} go on read the book" .format(student))