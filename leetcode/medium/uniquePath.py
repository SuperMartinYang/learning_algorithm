class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rowNum = len(obstacleGrid)
        colNum = len(obstacleGrid[0]) if rowNum > 0 else 0

        btou = [[None for _ in range(colNum)] for _ in range(rowNum)]
        # for i in range(n):
        #     btou[0][i] = 1
        # for j in range(m):
        #     btou[j][0] = 1
        for i in range(rowNum):
            for j in range(colNum):
                if obstacleGrid[i][j] == 1:
                    btou[rowNum - i - 1][colNum - j - 1] = 0
        if obstacleGrid[rowNum - 1][colNum - 1] == 0:
            btou[0][0] = 1
        else:
            btou[0][0] = 0

        def findPath(obstacleGrid, start_row, start_col):
            if start_row >= rowNum or start_col >= colNum:
                return 0
            if btou[rowNum - start_row - 1][colNum - start_col - 1] is not None:
                return btou[rowNum - start_row - 1][colNum - start_col - 1]
            else:
                res = findPath(obstacleGrid, start_row + 1, start_col) + findPath(obstacleGrid, start_row,
                                                                                  start_col + 1)
                btou[rowNum - start_row - 1][colNum - start_col - 1] = res
                return res

        return findPath(obstacleGrid, 0, 0)

    def uniquePathNoObstacles(self, m, n):
        """
        space m * n
        :param m:
        :param n:
        :return:
        """
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            res[i][0] = 1
        for i in range(n):
            res[0][i] = 1
        if res[m - 1][n - 1]:
            return res[m - 1][n - 1]
        res[m - 1][n - 1] = self.uniquePathNoObstacles(m - 1, n) + self.uniquePathNoObstacles(m, n - 1)
        return res[m - 1][n - 1]

    def uniquePathNoObstacles2(self, m, n):
        """
        space: n
        :param m: row
        :param n: col
        :return:
        """
        res = [0 for _ in range(n)]
        res[0] = 1
        for i in range(m):
            for j in range(1, n):
                res[j] += res[j - 1]
        return res[n - 1]


s = Solution()
# print(s.uniquePathsWithObstacles([[0],[0]]))
print(s.uniquePathNoObstacles2(10, 7))