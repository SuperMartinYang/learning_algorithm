class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        rows = len(forest)
        cols = len(forest[0]) if rows else 0
        visited = [[False] * cols for _ in range(rows)]
        memo = [[float('inf')] * cols for _ in range(rows)]
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or forest[i][j] <= 0:
                return float('inf')
            if visited[i][j]:
                return memo[i][j]
            visited[i][j] = True
            if forest[i][j] == 1:
                for p in direction:
                    memo[i][j] = min(memo[i][j], dfs(i + p[0], j + p[1]))
            else:
                for p in direction:
                    memo[i][j] = min(memo[i][j], 1 + dfs(i + p[0], j + p[1]))
            return memo[i][j]
        dfs(0, 0)
        return memo[0][0] if memo[0][0] != float('inf') else -1

print(Solution().cutOffTree([[1,1],[1,1]]))