def hanoi(n, from_, to_, aux_):
    if n == 1:
        print(from_, "->", to_)
        return
    
    hanoi(n - 1, from_, aux_, to_)

    print(from_, "->", to_)

    hanoi(n - 1, aux_, to_, from_)

print("n = 5")
hanoi(5, 1, 3, 2)