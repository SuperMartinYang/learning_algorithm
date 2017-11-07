class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        result = 0
        sign = 1
        for i in range(len(s)):
            if s[-i - 1] == '-':
                sign = -1
                continue
            result = int(s[-i - 1]) + result * 10
        return result == x

s = Solution()
print(s.isPalindrome(-1234321))