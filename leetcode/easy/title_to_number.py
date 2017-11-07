class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in s:
            sum = (ord(i) - 0x40) + sum * 26

        return sum