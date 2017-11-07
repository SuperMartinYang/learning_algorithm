class Solution(object):
    def reverse(self, x):
        """
        x = 4123
        result = 3214

        :type x: int
        :rtype: int
        """
        s = str(x)
        result = 0
        sign = 1
        for i in range(len(s)):
            if s[-i - 1] == '-':
                sign = -1
                continue
            result = int(s[-i - 1]) + result * 10
        if result > 2 << 30 :
            return 0
        return result * sign
s = Solution()
print(s.reverse(-321))