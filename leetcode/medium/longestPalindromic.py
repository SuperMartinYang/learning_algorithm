class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_rev = s[::-1]
        maxlength = 0
        palstr = ''
        for start in range(len(s)):
            for stop in range(start + 1, len(s) + 1):
                if s[start:stop] == s_rev[len(s) - stop: len(s) - start]:
                    length = stop - start
                    if length > maxlength:
                        palstr = s[start:stop]
        return palstr

s = Solution()
s.longestPalindrome('babad')