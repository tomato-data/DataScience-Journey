# r = read
score_file = open("score.txt", "r", encoding =  "utf8")
print(score_file.read())
score_file.close()

# 한 줄 한 줄
score_file = open("score.txt", "r", encoding =  "utf8")
print(score_file.readline(), end = "") # 한 줄 읽어오고 커서는 다음줄로 이동 -> maths: 0 영어로 넘어감
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())

# 몇 줄 인지 모를 때
score_file = open("score.txt", "r", encoding =  "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)

score_file.close()

score_file = open("score.txt", "r", encoding =  "utf8")
# list 형태로 저장
lines = score_file.readlines()
for line in lines:
    print(line, end = "")