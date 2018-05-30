class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i = 0
        j = 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
            i += 1
            if j == len(s):
                return True
        return False