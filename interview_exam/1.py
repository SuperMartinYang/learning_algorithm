import sys
import math
def solver(a, n):
    res = 0
    # indicate whether there exist odd number
    have = False
    for i in range(n):
        if a[i] % 2 == 0:
            res += a[i]
        else:
            res += a[i] - 1
            have = True
    return (res + 1) if have else res

# a = sys.stdin.readline().strip().split()
# a = [int(i) for i in a]
# print(a)
# print(solver(a, len(a)))


print(math.factorial(4))