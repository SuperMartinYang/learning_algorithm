class Solution(object):
    def solve(self, board):
        """
        dfs + backtracking return true or false, up down left right
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def helper(row, col):
            for r in range(len(board)):
                for c in range(len(board[0])):
                       dfs(r, c)

        def dfs(row, col):
            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
                return False
            if board[row][col] == 'O':
                board[row][col] = 'X'
                if dfs(row + 1, col) and dfs(row, col + 1) and dfs(row - 1, col) and dfs(row, col - 1):
                    return True
                else:
                    board[row][col] = 'O'
                    return False
            return True

        if len(board) == 0 or len(board[0]) == 0:
            return

        helper(0, 0)
        return board


print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))