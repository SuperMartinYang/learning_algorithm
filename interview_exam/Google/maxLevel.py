import math
def Solution(A):
    preSum = [0]
    for a in A:
        preSum.append(preSum[-1] + a)
    length = len(A)    
    level = 1
    maxVal = float("-inf")
    res = 0
    while (1 << level - 1) - 1 < length:
        val = (preSum[(1 << level) - 1] if (1 << level) - 1 <= length else preSum[-1]) \
                 - (preSum[(1 << level - 1) - 1] if (1 << level - 1) - 1 >= 0 else 0)
        if val > maxVal:
            maxVal = val
            res = level
        level += 1
    return res

print(Solution([0, 0, 1, 8,9]))