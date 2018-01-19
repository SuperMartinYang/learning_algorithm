class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowLen = len(matrix)
        colLen = len(matrix[0]) if rowLen > 0 else 0
        if rowLen == colLen == 0:
            return False

        def find(startRow, startCol, stopRow, stopCol):
            if startRow > stopRow or startCol > stopCol:
                return False
            if startRow == stopRow and startCol == stopCol:
                if target != matrix[startRow][startCol]:
                    return False
                else:
                    return True
            midRow = (stopRow + startRow) // 2
            midCol = (stopCol + startCol) // 2
            if target == matrix[midRow][midCol]:
                return True
            elif target < matrix[midRow][midCol]:
                return find(startRow, startCol, midRow, midCol)
            else:
                return find(startRow, midCol + 1, midRow, stopCol) or find(midRow + 1, startCol, stopRow, midCol) or find(
                    midRow + 1, midCol + 1, stopRow, stopCol)

        return find(0, 0, rowLen-1, colLen-1)


s = Solution()
print s.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
,5)
