def numberOfIslands(grid):
    # dfs to solve this problem
    m = len(grid)
    n = len(grid[0]) if m else 0
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(i, j, isldNum):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return isldNum
        grid[i][j] = 0
        res = 0
        for p, q in d:
            res = max(res, dfs(i + p, j + q, isldNum + 1))
        grid[i][j] = 1
        return res

    res = -1e9
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j, 0))
    return res


def numIsland(grid):
    m = len(grid)
    n = len(grid[0]) if m else 0
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    parent = [i for i in range(m * n)]
    rank = [0 for _ in range(m * n)]

    def union(x, y):
        px = find(x)
        py = find(y)
        if px != py:
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1

    def find(idx):
        if parent[idx] != idx:
            parent[idx] = find(parent[idx])
        return parent[idx]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                for p, q in d:
                    if 0 <= i + p < m and 0 <= j + q < n and grid[i + p][j + q] == 1:
                        union(i * n + j, (i + p) * n + (j + q))
    return max(map(parent.count, parent))


grid = [[0,1,1,1,0,0,0],
        [0,1,0,1,0,0,1],
        [0,0,1,1,0,0,1],
        [0,0,0,0,0,0,0]]
print(numberOfIslands(grid))
print(numIsland(grid))