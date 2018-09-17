class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        # write your code here
        # for each 0, we use dfs to update not -1 cell to be min
        m = len(rooms)
        n = len(rooms[0]) if m else 0
        d = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = [[False] * n for _ in range(m)]

        # dfs
        def dfs(i, j, cnt):
            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or rooms[i][j] == -1:
                return
            rooms[i][j] = min(rooms[i][j], cnt)
            visited[i][j] = True
            for p, q in d:
                dfs(i + p, j + q, cnt + 1)
            visited[i][j] = False

        # main
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)


Solution().wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])