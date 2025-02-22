import random

characters = list("abcdefghijklmnopqrstuvwxyz")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(characters) + random.choice(characters)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))