#coding=utf-8
import sys
def lucky(num):
    while num > 0:
        if num % 10 == 4 or num % 10 == 7:
            return True
        num //= 10
    return False

def solver(l, r):
    luck_nums = []
    res = 0
    for i in range(r + 1):
        if lucky(i):
            luck_nums.append(i)
    print(luck_nums)
    for i in range(len(luck_nums)):
        j = i
        while j < len(luck_nums):
            tmp = luck_nums[i] * luck_nums[j]
            while l <= tmp <= r:
                res += 1
                tmp *= luck_nums[j]
            j += 1
    return res

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip().split()
        line = [int(i) for i in line]
        print(line)
        print(solver(line[0], line[1]))