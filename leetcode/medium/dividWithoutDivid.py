class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend == float('-inf') and divisor == -1) or divisor == 0:
            return float('inf')
        res = 0
        sign = 1 if dividend > 0 and divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            tmp = divisor
            multi = 1
            while dividend >= divisor << multi:
                tmp <<= 1
                multi <<= 1
            dividend -= tmp
            res += multi
        return res * sign

s = Solution()
print(s.divide(-15, 3))