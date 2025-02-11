def nl(s_info: dict, num):
    if num in s_info:
        return s_info[num]
    else:
        return "?"

names = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(nl(names, 105))
print(nl(names, 777))