# O(logn)

def weigh(a, b, c, d):
    fake = 29
    if a <= fake <= b:
        return -1
    if c <= fake <= d:
        return 1
    return 0

def find_fakecoin(left, right):
    if left == right:
        return left
    
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1
    print(g1_left, g1_right, g2_left, g2_right)
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == 1:
        return find_fakecoin(g2_left, g2_right)
    elif result == -1:
        return find_fakecoin(g1_left, g1_right)
    else:
        return right


n = 100
print(find_fakecoin(0, n - 1))