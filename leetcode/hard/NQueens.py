import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        strArray = []
        occupied = [[0 for _ in range(n)] for _ in range(n)]
        self.backtrack(res, strArray, occupied, 0, n)
        return res

    def backtrack(self, res, strArray, occupied, line, n):
        if line == n:
            res.append(copy.deepcopy(strArray))
            return
        proto = '.' * n
        for i in range(n):
            if occupied[line][i] > 0:
                continue
            tmp = proto[:i] + 'Q' + proto[i + 1:]
            self.alterOccupied(occupied, i, line, True)
            strArray.append(tmp)
            self.backtrack(res, strArray, occupied, line + 1, n)
            self.alterOccupied(occupied, i, line, False)
            strArray.pop()

    def alterOccupied(self, occupied, col, row, signal):
        n = len(occupied)
        # # alter row
        # for i in range(n):
        #     occupied[row][i] = signal
        # # alter col
        for i in range(row + 1, n):
            occupied[i][col] += 1 if signal else -1
        # alter slash
        i = 0
        while i + col < n and i + row < n:
            occupied[i + row][i + col] += 1 if signal else -1
            i += 1
        i = 1
        while col - i >= 0 and i + row < n:
            occupied[i + row][col - i] += 1 if signal else -1
            i += 1

s = Solution()
print(s.solveNQueens(4))