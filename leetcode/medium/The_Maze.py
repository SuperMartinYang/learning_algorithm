class Solution(object):
    def the_maze(self, grid, i, j, x, y):
        """
        maze game with ball, using dfs
        :param grid: the map
        :param i: start row
        :param j: start col
        :param x: end row
        :param y: end col
        :return: bool
        """
        m = len(grid)
        n = len(grid[0]) if m else 0
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp = [[-1] * n for _ in range(m)]

        def dfs(ni, nj):
            if ni == x and nj == y: return True
            if dp[ni][nj] != -1: return dp[ni][nj]
            res = False
            grid[ni][nj] = -1 # mask
            # can stop
            for p in d:
                ti, tj = ni, nj
                # roll
                while 0 <= ti < m and 0 <= tj < n and grid[ti][tj] != 1:
                    ti += p[0]
                    tj += p[1]
                ti -= p[0]      # move back from wall
                tj -= p[1]
                if grid[ti][tj] != -1:    # no visited
                    res = res or dfs(ti, tj)
            dp[ni][nj] = res
            return res

        return dfs(i, j)

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
print(Solution().the_maze(grid, si, sj, ex1, ey1))