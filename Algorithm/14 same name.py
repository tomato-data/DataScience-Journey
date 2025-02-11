def sn(l: list):
    name_dict = {}
    for i in l:
        if i not in name_dict:
            name_dict[i] = 1
        elif i in name_dict:
            name_dict[i] += 1
    ans = []
    for j in name_dict:
        if name_dict[j] >= 2:
            ans.append(j)
    return ans

names = ["Tom", "Jerry", "Mike", "Tom"]
print(sn(names))

names2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(sn(names2))