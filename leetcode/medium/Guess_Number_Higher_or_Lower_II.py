class Solution(object):
    def guess_number_higher_or_lower_ii(self, n):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                # bottom-up
                if j + 1 == i:
                    dp[j][i] = j
                    continue
                gm = float('inf')
                for k in range(j + 1, i):
                    # pick any number in (j + 1, i - 1), then get the max between the min of each part,
                    # because we don't know which the guessing number locate
                    # then update dp[j][i] with minimum spend
                    tmp = k + max(dp[j][k - 1], dp[k + 1][i])
                    gm = min(gm, tmp)
                dp[j][i] = gm
        return dp[1][n]
