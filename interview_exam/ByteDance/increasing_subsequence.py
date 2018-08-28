# non decrease subsequence
import sys


def solve(nums):
    dp = [1] * len(nums)
    res = -1e9
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res


if __name__ == "__main__":
    a = sys.stdin.readline().strip().split()
    n, t = int(a[0].strip()), int(a[1].strip())
    line = sys.stdin.readline().strip()
    nums = map(int, line.split()) * t
    print(solve(nums))
    # print ans