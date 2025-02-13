try:
    print("one digit division only")
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))

except ValueError:
    print("wrong value input")