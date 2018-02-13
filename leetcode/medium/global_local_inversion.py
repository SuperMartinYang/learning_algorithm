class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        NList = [i for i in range(len(A))]

        def updateNList(num):
            for i in range(num + 1, len(A)):
                NList[i] -= 1

        innerCnt = 0
        globCnt = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                innerCnt += 1

        for i in range(len(A)):
            globCnt += NList[A[i]]
            updateNList(A[i])
        return innerCnt == globCnt

s = Solution()
print(s.isIdealPermutation([1,0,2]))