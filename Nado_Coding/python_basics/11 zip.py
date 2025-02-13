kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))
# [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

kor2, eng2 = list(zip(*mixed))

print(kor2)
print(eng2)