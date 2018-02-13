class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLen = len(needle)
        if len(haystack) < needleLen:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and (i + needleLen - 1 < len(haystack)):
                if haystack[i: i + len(haystack)] == needle:
                    return i
        return -1

s = Solution()
print(s.strStr('hello', 'll'))