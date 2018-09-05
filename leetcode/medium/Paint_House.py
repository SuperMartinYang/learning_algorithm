import copy
class Solution(object):
    def paint_house(self, costs):
        """
        paint house with no same color for adjacent houses. minimize the cost
        :param costs: House Num i + Color j -> Cost i, j
        :return: minimum cost
        """
        dp = copy.deepcopy(costs)
        for i in range(1, len(costs)):
            for j in range(3):
                dp[i][j] += min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
        return min(dp[len(costs) - 1])

print(Solution().paint_house())