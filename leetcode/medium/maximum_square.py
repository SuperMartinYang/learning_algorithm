def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    def maximal(start_row, start_col, matrix):
        if start_col >= len(matrix[0]) or start_row >= len(matrix):
            return 0
        if matrix[start_row][start_col] == '0':
            return 0
        else:
            i = 1
            out = 1
            while True:
                if start_row + i < len(matrix) and start_col + i < len(matrix[0]):
                    for x in range(i + 1):
                        if matrix[start_row + i][start_col + x] == '0' or matrix[start_row + x][start_col + i] == '0':
                            return out
                    i += 1
                    out = i * i
                else:
                    return max(out, 1)
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    result = 0

    for i in range(row):
        for j in range(col):
            result = max(maximal(i, j, matrix), maximal(i + 1, j, matrix),
                         maximal(i, j + 1, matrix),result)
    return result

print(maximalSquare([["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]))