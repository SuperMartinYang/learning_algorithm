class Solution(object):
    def paint_fence(self, n, k):
        if n == 0: return 0
        same, dif = 0, k
        for i in range(2, n + 1):       # dif means different from i - 2, same means equals to i - 1
            t = dif
            dif = (same + dif) * (k - 1)
            same = t
        return same + dif

    def paint_fence_with_extra_space(self, n, k):
        if n == 0: return 0
        # dp[i][0], ith post is the same color as previous, dp[i][1] means ith post is different as pre
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 0; dp[0][1] = 0
        dp[1][0] = 0; dp[1][1] = k
        for i in range(2, n + 1):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) * (k - 1)
        return dp[n][0] + dp[n][1]


print(Solution().paint_fence(2, 5))
print(Solution().paint_fence_with_extra_space(2, 5))
