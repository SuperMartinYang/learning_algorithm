class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def backtrack(permuteStr, tmpStr, n, k):
            if len(tmpStr) == n:
                permuteStr.append(tmpStr)
                if len(permuteStr) == k:
                    return True
            for i in range(1, n + 1):
                if tmpStr.find(str(i)) != -1:
                    continue
                tmpStr += str(i)
                if backtrack(permuteStr, tmpStr, n, k):
                    return True
                tmpStr = tmpStr[:-1]

        permuteStr = []
        backtrack(permuteStr, '', n, k)
        return permuteStr.pop()


# Clever myself
from math import factorial
class Solution2(object):
    def getPermutation(self, n, k):
        nums = [i for i in range(1, n + 1)]
        res = ''
        while k and n:
            fac = factorial(n - 1)
            index = (k - 1) // fac
            k -= index * fac
            n -= 1
            res += str(nums.pop(index))
        return res

s = Solution2()
print s.getPermutation(9, 54494)