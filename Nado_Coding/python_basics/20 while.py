customer = "a"
index = 5

while index >= 1:
    print("{0}, coffee ready. {1} times left." .format(customer, index))
    index -= 1 
    if index == 0:
        print("coffee wasted")

# customer = "b"
# index = 1

# while True:
#     print("{0}, coffee ready. {1} time(s)" .format(customer, index))
#     index += 1

customer = "c"
person = "unknown"

while person != customer:
    print("{0}, coffee ready." .format(customer))
    person = input("what is your name?" )
    if person == customer:
        print("there you go")