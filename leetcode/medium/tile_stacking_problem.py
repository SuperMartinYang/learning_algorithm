#!/bin/python3

import sys

# sub_problem
def stacking(n, bot, bot_count, m, k):
    if n == 0:
        return 1
    totle = 0
    new_bot = m
    min_bot = n // k if n % k == 0 else n // k + 1
    while new_bot >= min_bot:
        bot_cnt = k-1
        while bot_cnt > 0:
            totle += stacking(n - 1, new_bot, bot_cnt, new_bot - 1, k)
            bot_cnt -= 1
        new_bot -= 1
    totle += stacking(n - 1, bot, bot_count - 1, m, k)
    return totle

def tileStackingProblem(n, m, k):
    # Complete this function
    # sub_problem, without bottom=> stacking(n-1, m, k-1, m-1, k)
    bot = m
    totle = 0
    min_bot = n // k if n % k == 0 else n // k + 1
    while bot >= min_bot:
        bot_cnt = k-1
        while bot_cnt >= 0:
            totle += stacking(n - 1, bot, bot_cnt, bot - 1, k)
            bot_cnt -= 1
        bot -= 1
    return totle % (pow(10, 9) + 7)


dic = {}
dic.keys()

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    result = tileStackingProblem(n, m, k)
    print(result)
