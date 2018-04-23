#coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    dayGrowth = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        values = [i for i in values]
        if values[0] == 1:  # from to
            # form a day growth rule
            if values[2] > len(dayGrowth):
                newDayGrowth = [float('-inf') for _ in range(values[2])]
                for i in range(len(dayGrowth)):
                    newDayGrowth[i] = dayGrowth[i]
            for j in range(values[1] - 1, values[2]):
                if newDayGrowth[j] < values[3]:
                    newDayGrowth[j] = values[3]
            dayGrowth = newDayGrowth
        if values[0] == 2:  # activity
            ans += values[2]
    for i in range(len(dayGrowth)):
        if dayGrowth[i] == float('-inf'):
            dayGrowth[i] = 0
    ans += sum(dayGrowth)
    print(ans)