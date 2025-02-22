key_list = ["name", "hp", "mp", "level"]
value_list = ["knight", 200, 30, 5]
character = {}

for i in range(3):
    character[key_list[i]] = value_list[i]

print(character)

limit = 10000
i = 1
sum_value = 0

while sum_value < limit:
    sum_value += i
    i += 1

    if sum_value >= limit:
        print("when you add {}, it exceeds {} and the value would be {}"\
            .format(i - 1, limit, sum_value))
        break

max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("it becomes maximum when: {} * {} = {}".format(a, b, max_value))
