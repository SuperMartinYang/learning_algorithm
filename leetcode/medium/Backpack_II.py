class Solution(object):
    def backpack_ii(self, vol, weight, total):
        """

        :param vol: volume for each item
        :param weight: weight for each item
        :param total: total volume
        :return:
        """
        dp = [[0] * len(vol) for _ in range(total + 1)]
        for i in range(1, total + 1):
            for j in range(len(weight)):
                dp[i][j] = max(dp[i - vol[j]][j - 1] + weight[j] if i >= vol[j] else 0, dp[i][j - 1])
        return dp[total][len(weight) - 1]


print(Solution().backpack_ii([3,5,2], [18, 2, 4], 5))