class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        res = []

        def dfs(r, c, visited, pre):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1 or visited[r][c] or matrix[r][c] < pre:
                return

            visited[r][c] = True
            dfs(r + 1, c, visited, matrix[r][c])
            dfs(r - 1, c, visited, matrix[r][c])
            dfs(r, c + 1, visited, matrix[r][c])
            dfs(r, c - 1, visited, matrix[r][c])

        for i in range(m):
            dfs(i, 0, p_visited, float('-inf'))
            dfs(i, n - 1, a_visited, float('-inf'))

        for i in range(n):
            dfs(0, i, p_visited, float('-inf'))
            dfs(m - 1, i, a_visited, float('-inf'))


        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])

        return res


print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))