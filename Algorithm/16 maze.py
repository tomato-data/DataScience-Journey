def solve_maze(ma: dict, start, end):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        print(qu)
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in ma[v]:
            if x not in done:
                qu.append(p + x)
                done.add(x)
    
    return "?"

maze = {
    "a": ["e"],
    "e": ["i"],
    "i": ["m"],
    "m": ["i", "n"],
    "n": ["m", "j"],
    "j": ["n", "k", "f"],
    "k": ["o", "j"],
    "o": ["k"],
    "f": ["b", "g", "j"],
    "b": ["c", "f"],
    "c": ["b", "d"],
    "d": ["c"],
    "g": ["f", "h"],
    "h": ["g", "l"],
    "l": ["h", "p"],
    "p": ["l"]
}

print(solve_maze(maze, "a", "p"))