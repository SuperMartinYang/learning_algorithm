class UnionFind(object):
    def __init__(self, m, n, grid):
        self.root = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(n):
            if grid[0][i] == 1:
                self.root[i] = i

    # def union(self, ):

class Solution(object):
    def from_1st_row_to_lst_row(self, grid):
        # DFS with memo
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        # get starting points here
        visited = set()    # i, j in set means visited
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c > cols or grid[r][c] != 1 or (r, c) in visited:
                return False
            if r == rows - 1: return True
            visited.add((r, c))
            for p in d:
                if dfs(r + p[0], c + p[1]):
                    return True
            # visited.remove((r, c))
            return False

        for i in range(cols):
            if grid[0][i] == 1:
                # dfs
                if dfs(0, i):
                    return True
        return False

    def from_1st_row_to_lst_row_uf(self, grid):
        # TODO
        return

grid = [[0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,1,0,0,0]]
print(Solution().from_1st_row_to_lst_row(grid))