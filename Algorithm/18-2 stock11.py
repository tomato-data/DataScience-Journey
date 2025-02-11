def max_profit(l: list):
    n = len(l)
    max_p = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if l[j] - l[i] > max_p:
                max_p = l[j] - l[i]

    return max_p

def max_profit_a(l: list):
    n = len(l)
    max_p = 0
    min_price = l[0]
    for i in range(1, n):
        profit = l[i] - min_price
        if profit > max_p:
            max_p = profit
        if l[i] < min_price:
            min_price = l[i]

    return max_p

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
print(max_profit_a(stock))