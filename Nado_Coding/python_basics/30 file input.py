# w = 쓰기 but 다시 사용하면 덮어쓰기가 됨
score_file = open("score.txt", "w", encoding = "utf8")
print("maths: 0", file = score_file)
print("English: 50", file = score_file)
score_file.close()

# a도 쓰기지만 이어쓰기 (append)
score_file = open("score.txt", "a", encoding = "utf8")

# 위의 케이스와는 다르게 자동으로 줄바꿈이 되지 않음. (end = "")
score_file.write("science: 80")
score_file.write("\ncoding: 100")
score_file.close()