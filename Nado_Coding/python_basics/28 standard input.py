import sys
print("java", "python", file = sys.stdout) # 표준 출력
print("java", "python", file = sys.stderr) # 표준 에러

# sep 로 콤마가 어떤 기능을 할지 선택 가능
print("java", "python", sep = "vs", end = "?")

score = {"Maths" : 0, "English": 50, "Coding": 100}
for subject, score in score.items(): # items = 키와 밸류 쌍으로 나옴
    # 8칸 확보하고 왼쪽 정렬
    print(subject.ljust(10), str(score).rjust(4 ), sep = ":")

for num in range(1, 21):
    # zfill로 0을 채움
    print("waiting number: " + str(num).zfill(3))

# input = str value
answer = input("enter any value: ")
print(type(answer))
print("entered value is {}".format(answer))