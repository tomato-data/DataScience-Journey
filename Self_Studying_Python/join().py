print("::".join(["1", "2", "3", "4", "5"]))

# join 을 활용해서 아래와 같이 여러 줄 문자열을 정리.
number = int(input("integral>"))

if number % 2 == 0:
    print("\n".join([
        "given integral is {}",
        "{} is an even number"
    ]).format(number, number))

else:
    print("\n".join([
        "given integral is {}",
        "{} is an odd number"
    ]).format(number, number))