class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        _dp = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(r, c, pre):
            if r < 0 or r > row - 1 or c < 0 or c > col - 1 or matrix[r][c] == '*' or matrix[r][c] <= pre:
                return 0
            if _dp[r][c]:
                return _dp[r][c]
            tmp = matrix[r][c]
            matrix[r][c] = '*'
            down = dfs(r + 1, c, tmp)
            right = dfs(r, c + 1, tmp)
            up = dfs(r - 1, c, tmp)
            left = dfs(r, c - 1, tmp)
            matrix[r][c] = tmp
            _dp[r][c] = 1 + max(down, right, up, left)
            return _dp[r][c]

        res = 0
        for i in range(row):
            for j in range(col):
                if not _dp[i][j]:
                    res = max(res, dfs(i, j, float('-inf')))
        return res


print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
