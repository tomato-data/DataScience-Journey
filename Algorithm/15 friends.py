fr_info = {
    "Summer": ["John", "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["Summer", "John", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]
}

def all_fr(frnds: dict, start):
    qu = []
    done = set()
    qu.append((start, 0))
    done.add(start)
    while qu:
        p, d = qu.pop(0)
        print(p, d)
        for x in frnds[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)


all_fr(fr_info, "Summer")
print()
all_fr(fr_info, "Jerry")