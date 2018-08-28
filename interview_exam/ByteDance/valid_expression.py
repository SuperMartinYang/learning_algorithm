import sys

def solve(cnt):
    dp = [0] * (cnt + 1)
    dp[1] = 10
    for i in range(2, cnt + 1):
        dp[i] = 10 * dp[i - 1] + 21 * dp[i - 2]
        # x + y or x - y
    return dp[cnt] % 1000000007

for line in sys.stdin:
    cnt = int(line.strip())
    print(solve(cnt))