class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        keys = set()
        memo = [[float('inf')] * cols for _ in range(rows)]
        keys_required = sum([1 for i in range(rows) for j in range(cols) if grid[i][j].isalpha()]) / 2

        def dfs(r, c, remain):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '#' or 'A' <= grid[r][c] <= 'F' and grid[r][c].lower() not in keys:
                return float('inf')
            elif not memo[r][c] or memo[r][c] == float('inf'):
                if 'a' <= grid[r][c] <= 'f':
                    keys.add(grid[r][c])
                    remain -= 1
                    if remain == 0: return 1
                if 'A' <= grid[r][c] <= 'F':
                    keys.remove(grid[r][c].lower())
                for p in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    memo[r][c] = min(memo[r][c], 1 + dfs(r + p[0], c + p[1], remain))
                
            return memo[r][c]

        dfs(0, 0, keys_required)
        return memo

print(Solution().shortestPathAllKeys(['@.a.#', '###.#', 'b.A.B']))