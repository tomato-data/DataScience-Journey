try:
    number_input_a = int(input("integral> "))

except:
    print("not integral")

else:
    print("radius", number_input_a)
    print("circumference", 2 * 3.14 * number_input_a)
    print("area", 3.14 * number_input_a * number_input_a)