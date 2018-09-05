class Solution(object):
    def edit_distance(self, str1, str2):
        # dp solution
        m = len(str1)
        n = len(str2)
        # dp[i][j] means min steps str1[..i] can be edited to str2[..j]
        dp = [[1e9] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(m): dp[i + 1][0] = i + 1
        for j in range(n): dp[0][j + 1] = j + 1
        for i in range(m):
            for j in range(n):
                # equal
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                # replace / insert / delete
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1],    # delete
                                           dp[i + 1][j],    # insert
                                           dp[i][j]) + 1    # replace

        return dp[m][n]

print(Solution().edit_distance('abc','bcd'))