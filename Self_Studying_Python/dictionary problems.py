pets = [
    {"name": "cloud", "age": 5},
    {"name": "choco", "age": 3},
    {"name": "aji", "age": 1},
    {"name": "tiger", "age": 1}
]

for pet_info in pets:
        print(pet_info["name"], str(pet_info["age"]) + "살")

numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}


for number in numbers:
    counting = numbers.count(number)
    counter[number] = counting

print(counter)

character = {
    "name": "knight",
    "level": 12,
    "items": {
        "sword": "fire sword",
        "armor": "plate armor"
    },
    "skill": ["cut", "strong cut", "very strong cut"]
}

for key in character:
    if type(character[key]) is str or type(character[key]) is int:
        print(key + " : " + str(character[key]))
    elif type(character[key]) is dict:
        for item in character[key]:
            print(item + " : " + character[key][item])
    elif type(character[key]) is list:
        for skill in character[key]:
            print(key + " : " + skill)

