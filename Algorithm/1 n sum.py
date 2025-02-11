def n_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(n_sum(100))

# n_sum은 숫자가 커질수록 그만큼 덧셈을 해야하지만 
# n_sum2는 곱셈, 덧셈, 나눗셈 한번씩만 하면 돼서 더 효율적
def n_sum2(n):
    return n * (n + 1) // 2