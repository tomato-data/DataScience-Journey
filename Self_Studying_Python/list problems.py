list_c = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for element in list_c:
    if element % 2 == 0:
        print(str(element) + " is even number")
    else:
        print(str(element) + " is odd number")

for element in list_c:
    if len(str(element)) == 3:
        print(str(element) + " is 3 digit number")
    elif len(str(element)) == 2:
        print(str(element) + " is 2 digit number")
    elif len(str(element)) == 1:
        print(str(element) + " is 1 digit number")

list_of_lists = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

for lst in list_of_lists:
    for element in lst:
        print(element)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number)

print(output)