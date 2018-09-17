class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        # use 2-D array
        dp = [[0] * len(A) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(len(A)):
                dp[i][j] = max(dp[i - A[j]][j - 1] + A[j] if i >= A[j] else 0, dp[i][j - 1])
        return dp[m][len(A) - 1]

print(Solution().backPack(11, [1,10]))