import sys
import math

def cal(t, times, outer, score):
    c = math.factorial(times) / (math.factorial(times - t) * math.factorial(t))
    p = c * outer ** t * score
    return p

def solver(circle_num, area, times, score):
    # percent = area[i] / area[-1]
    outer = (area[-1] - area[-2]) / area[-1]
    for i in range(times):
        res = cal(i, times, outer, score)
        res += solver(circle_num - 1, area[:circle_num - 1], times - i, score + 1)
    return res

if __name__ == '__main__':
    circle_num = int(sys.stdin.readline().strip())
    ri = sys.stdin.readline().strip().split()
    ri = [int(i) for i in ri]
    area = [i * i for i in ri]
    times = int(sys.stdin.readline().strip())
    print(solver(area, ri, times, 1))