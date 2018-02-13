class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        rowLen = len(matrix)
        colLen = len(matrix[0]) if rowLen > 0 else 0
        # if rowLen == 1:
        #     return matrix[0]
        # if colLen == 1:
        #     return [matrix[i][0] for i in range(rowLen)]
        i = 0
        while i * 2 < rowLen and i * 2 < colLen:
            if i == colLen - i - 1:
                for j in range(i, rowLen - i):
                    res.append(matrix[j][i])
            elif i == rowLen - i - 1:
                for j in range(i, colLen - i):
                    res.append(matrix[i][j])
            else:
                # right
                for j in range(i, colLen - i - 1):
                    res.append(matrix[i][j])
                # down
                for j in range(i, rowLen - i - 1):
                    res.append(matrix[j][colLen - i - 1])
                # left
                for k in range(i, colLen - i - 1):
                    res.append(matrix[rowLen - i - 1][colLen - k - 1])
                # up
                for z in range(i, rowLen -i - 1):
                    res.append(matrix[rowLen - z - 1][i])
            i += 1
        return res

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]))