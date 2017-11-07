from math import *
class Solution(object):
    def climbStairs(self, n):
        """
        climb stair can be looked as divide sticks, C(0...(n-1)/2, n-1...(n-1)/2)
        :type n: int
        :rtype: int
        """
        result = 0
        if n == 1:
            return 1
        for i in range(int((n + 1) / 2) + 1):
            if i <= n - i:
                result += self.C(i, n - i)
        return result
    def C(self, up, down):
        return factorial(down)/(factorial(down-up)* factorial(up))


s = Solution()
print(s.climbStairs(3))
