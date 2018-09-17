class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        # find enermy and update its column and row
        m = len(grid)
        n = len(grid[0]) if m else 0

        def update(i, j):
            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # update col
            for p, q in d[:2]:
                r, c = i, j
                while 0 <= r + p < m and grid[r + p][c + q] != 'W':
                    r += p
                    c += q
                    if grid[r][c] == 'E': continue
                    grid[r][c] = str(int(grid[r][c]) + 1)

            # update row
            for p, q in d[2:]:
                r, c = i, j
                while 0 <= c + q < n and grid[r + p][c + q] != 'W':
                    r += p
                    c += q
                    if grid[r][c] == 'E': continue
                    grid[r][c] = str(int(grid[r][c]) + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'E':
                    update(i, j)
        res = -1e9
        for i in range(m):
            for j in range(n):
                if grid[i][j].isdigit():
                    res = max(res, int(grid[i][j]))

        return res


class Solution1:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def maxKilledEnemies(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0]) if m else 0
        res = 0
        for i in range(m):
            st, ed = 0, 0
            rowCnt = 0
            while ed <= n:
                if ed == n or grid[i][ed] == 'W':
                    for j in range(st, ed):
                        if grid[i][j].isdigit():
                            newVal = int(grid[i][j]) + rowCnt
                            res = max(newVal, res)
                            grid[i][j] = str(newVal)
                    rowCnt = 0
                    st = ed + 1
                elif grid[i][ed] == 'E':
                    rowCnt += 1
                ed += 1

        for i in range(n):
            st, ed = 0, 0
            colCnt = 0
            while ed <= m:
                if ed == m or grid[ed][i] == 'W':
                    for j in range(st, ed):
                        if grid[j][i].isdigit():
                            newVal = int(grid[j][i]) + colCnt
                            res = max(newVal, res)
                            grid[j][i] = str(newVal)
                    colCnt = 0
                    st = ed + 1
                elif grid[ed][i] == 'E':
                    colCnt += 1
                ed += 1
        return res

# print(Solution1().maxKilledEnemies([['0','E','0','0'],['E','0','W','E'], ['0','E','0','0']]))
print(Solution1().maxKilledEnemies(["W00000EEEEEEEE000000WWW0WWW00W0W0WEEEE0000EW00W"]))
