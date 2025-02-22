array = ["apple", "plum", "chocolate", "banana", "cherry"]

# array의 요소를 fruit 이라고 할 때 초콜릿이 아닌 fruit 으로 리스트를 재조합 해주세요
output = [fruit for fruit in array if fruit != "chocolate"]

print(output)