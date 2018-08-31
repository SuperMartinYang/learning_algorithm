class Solution(object):
    def predict_the_winner(self, nums):
        """

        :param nums: numbers available to choose
        :return: bool
        """
        dp = {}
        def getPOrN(i, j):
            """
            :param nums: numbers remain
            :return: one player can get minus the other one, positive or negative
            """
            if (i, j) not in dp:
                if i == j: return nums[i]
                dp[i, j] = max(nums[i] - getPOrN(i + 1, j), nums[j] - getPOrN(i, j - 1))
            return dp[i, j]
        return getPOrN(0, len(nums) - 1) >= 0


print(Solution().predict_the_winner([1,5,233, 7]))