# concat, see whether in it

import sys

def canBe(a, b):
    # shift b
    if len(a) != len(b): return False
    for i in range(len(a)):
        shiftb = b[i:] + b[:i]
        if shiftb[::-1] == a or shiftb == a:
            return True
    return False

def solve(d):
    for i in range(len(d)):
        for j in range(i + 1, len(d)):
            if canBe(d[i], d[j]):
                return "Yeah"
    return "Sad"

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(t):
        # read three line
        n = int(sys.stdin.readline().strip())
        d = []
        for j in range(n):
            d.append(sys.stdin.readline().strip() * 2)
        print(solve(d))