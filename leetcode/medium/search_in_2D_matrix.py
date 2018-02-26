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

    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowLen = len(matrix)
        colLen = len(matrix[0]) if rowLen > 0 else 0
        if not rowLen or not colLen:
            return False

        def findrow():
            rlo, rhi = 0, rowLen - 1
            while rlo + 1 < rhi:
                rmid = (rhi - rlo) // 2 + rlo
                if matrix[rmid][0] <= target <= matrix[rmid][colLen - 1]:
                    return rmid
                elif target > matrix[rmid][colLen - 1]:
                    rlo = rmid
                elif target < matrix[rmid][0]:
                    rhi = rmid
            if matrix[rlo][0] <= target <= matrix[rlo][colLen - 1]:
                return rlo
            if matrix[rhi][0] <= target <= matrix[rhi][colLen - 1]:
                return rhi
            return -1

        def findcol(rowNo):
            clo, chi = 0, colLen - 1
            while clo + 1 < chi:
                cmid = (chi - clo) // 2 + clo
                if matrix[rowNo][cmid] == target:
                    return True
                elif target > matrix[rowNo][cmid]:
                    clo = cmid
                else:
                    chi = cmid
            if matrix[rowNo][clo] == target: return True
            if matrix[rowNo][chi] == target: return True
            return False

        rowNo = findrow()
        return findcol(rowNo) if rowNo != -1 else False

    def searchMatrix2(self, matrix, target):
        """
        treat as sorted array
        """
        rowLen = len(matrix)
        colLen = len(matrix[0]) if rowLen else 0
        if not rowLen or not colLen:
            return False
        tot_no = rowLen * colLen
        lo, hi = 0, tot_no - 1
        while lo + 1 < hi:
            mid = (hi - lo) // 2 + lo
            midRow = mid // colLen
            midCol = mid % colLen
            if target > matrix[midRow][midCol]:
                lo = mid
            elif target < matrix[midRow][midCol]:
                hi = mid
            else:
                return True
        if matrix[lo // colLen][lo % colLen] == target: return True
        if matrix[hi // colLen][hi % colLen] == target: return True
        return False


s = Solution()
print(s.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],5))
