def s_algo(d: dict, start):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    while qu:
        r = qu.pop(0)
        print(r)
        for x in d[r]:
            if x not in done:
                qu.append(x)
                done.add(x)

example = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

print(s_algo(example, 1))