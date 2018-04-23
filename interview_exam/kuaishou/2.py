#coding=utf-8
import sys

def bf(values, n):
    lo, hi = 0, len(values) - 1
    while lo < hi - 1:
        mid = (hi - lo) // 2 + lo
        if values[mid] == n:
            return mid
        elif values[mid] > n:
            hi = mid
        else:
            lo = mid
    if values[lo] >= n: return lo
    if values[hi] >= n: return hi
    return hi + 1

if __name__ == "__main__":
    # 读取第一行的n
    ans = 0
    line = sys.stdin.readline().strip().split()
    values = [int(i) for i in line]
    n = int(sys.stdin.readline().strip())
    ans = bf(values, n)
    print(ans)