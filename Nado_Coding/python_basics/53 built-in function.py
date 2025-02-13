# 따로 import 할 필요없이 사용가능한 함수
# ex) input
# dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려 줌


print(dir())
import random # 외장함수
print(dir())
import pickle
print(dir())

# 랜덤 모듈 내에서 쓸 수 있는 것들을 알려줌
print(dir(random))

# list 에서 쓸 수 있는 것들
lst = [2, 3, 4]
print(dir(lst))

name = "jim"
print(dir(name))

# 구글에 list of python builtins 검색 -> 내장함수 내용 검색 가능