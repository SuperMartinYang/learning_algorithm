class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rowLen = len(board)
        colLen = len(board[0])

        def isValid(row, col, ch):
            for i in range(rowLen):
                if board[row][i] != '.' and board[row][i] == ch: return False
                if board[i][col] and board[i][col] == ch: return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and ch == board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3]: return False
            return True

        def solve():
            for i in range(rowLen):
                for j in range(colLen):
                    if board[i][j] == '.':
                        for k in range(ord('1'), ord('9') + 1):
                            if isValid(i, j, chr(k)):
                                board[i][j] = chr(k)
                                if solve():
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        solve()

print(Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
))
