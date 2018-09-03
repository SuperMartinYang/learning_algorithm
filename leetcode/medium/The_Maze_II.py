class Solution(object):
    def the_maze_ii(self, grid, i, j, x, y):
        """
        DFS, when deeper, count when roll, memo to memoize result of path passed, return minimum
        :param grid: 2D list, maze
        :return: shortest path to there
        """
        m = len(grid)
        n = len(grid[0]) if m else 0
        memo = [[1e9] * n for _ in range(m)]
        memo[i][j] = 0
        d = ((1, 0), (0, 1), (0, -1), (-1, 0))

        def dfs(ni, nj):
            if ni == x and nj == y: return
            # no need to memo whether we visited it before. because we may from a shorter path to a certain point
            for p in d:
                ti, tj, cnt = ni, nj, memo[ni][nj]
                while 0 <= ti + p[0] < m and 0 <= tj + p[1] < n and grid[ti + p[0]][tj + p[1]] != 1:
                    ti += p[0]
                    tj += p[1]
                    cnt += 1
                if memo[ti][tj] > cnt:
                    memo[ti][tj] = cnt
                    dfs(ti, tj)
        dfs(i, j)
        return memo[x][y] if memo[x][y] != 1e9 else -1

grid = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
si = 0
sj = 4
ex = 3
ey = 2

ex1 = 4
ey1 = 4
print(Solution().the_maze_ii(grid, si, sj, ex1, ey1))