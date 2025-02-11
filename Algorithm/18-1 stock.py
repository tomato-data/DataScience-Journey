# 풀기 전 혼자
# O(n ** 2)
def max_profit(prices: list):
    mp = 0
    n = len(prices)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if prices[j] - prices[i] > mp:
                mp = prices[j] - prices[i]
    return mp

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))