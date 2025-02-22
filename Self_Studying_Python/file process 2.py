with open("info.txt", "r") as file:
    for line in file:
        name, weight, height = line.strip().split(", ")

        if not name or not weight or not height:
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "overweight"
        elif 18.5 <= bmi:
            result = "normal"
        else:
            result = "underweight"

        print('\n'.join([
            "name: {}",
            "weight: {}",
            "height: {}",
            "BMI: {}",
            "result: {}"
        ]).format(name, weight, height, bmi, result))
        print()