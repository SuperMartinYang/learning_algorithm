class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x = n ^ m
        mask = 0
        while x > 0:
            x >>= 1
            mask = (mask << 1) + 1
        return m & (~mask)