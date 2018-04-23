class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        init = [1]
        for i in range(1, rowIndex + 1):
            res = [0 for _ in range(i + 1)]
            for j in range(i + 1):
                res[j] = init[j] + init[j - 1] if j - 1 >= 0 and j < len(init) else 1
            init = res
        return res


s = Solution()
print(s.getRow(6))