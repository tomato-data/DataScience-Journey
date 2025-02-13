from random import *
print(random()) # 0~1 사이의 임의의 값 생성
print(random() * 10)
print(int(random() * 10)) # 0 부터 10 미만의 정수 생성
print(int(random() * 10) + 1) #  0 부터 10이하(11미만)의 정수 생성
print(randrange(1, 46)) # 1 ~ 45이하(46미만)의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45이하의 숫자 생성