class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def helper(m):
            if m == 1:
                return 0
            if m in dp:
                return dp[m]
            if m % 2 == 0:
                dp[m] = 1 + helper(m // 2)
            else:
                dp[m] = min(helper(m - 1), helper(m + 1)) + 1
            return dp[m]
        return helper(n)