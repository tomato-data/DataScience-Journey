python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 첫 알파벳이 대문자인가
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) # 파이썬이란 변수에서 n 이 몇번째에 위채해있는지 확인
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 없으면 -1을 반환

# print(python.index("Java")) # 없으면 에러

print(python.count("n")) # 문자열에서 원하는게 몇개나 있는지 세어줌