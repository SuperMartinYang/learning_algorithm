#coding=utf-8
import sys
import math

def SQM(x, b, n):
    u = 1
    k = int(math.log2(b))

    for i in range(k, -1, -1):
        u = (u * u) % n
        if b & (1 << i) == (1 << i):
            u = (u * x) % n
    return u

if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip().split()
    # 把每一行的数字分隔后转化成int列表
    values = [int(i) for i in line]
    x = values[0]
    y = values[1]
    n = values[2]
    ans = SQM(x, y, n)
    print(ans)
