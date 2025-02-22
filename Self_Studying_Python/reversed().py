temp = reversed([1, 2, 3, 4, 5, 6])

# 밑의 코드 중 첫번째 반복문만 실행 됨
# reversed 함수와 반복문을 조합할 때는 함수의 결과를 여러번 활용 X
# 직접 필요한 시점에 reversed 함수 사용

for i in temp:
    print("first iteration: {}".format(i))

for i in temp:
    print("second iteration: {}".format(i))
