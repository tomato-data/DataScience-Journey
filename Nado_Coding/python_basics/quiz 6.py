def std_weight(height, gender):
    if gender == "F":
        return height* height * 21
    elif gender == "M":
        return height * height * 22
    else:
        print("wrong input")

height = 178
gender = "M"

weight = round(std_weight(height / 100, gender), 2)
print(weight)