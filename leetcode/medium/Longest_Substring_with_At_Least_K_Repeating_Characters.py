class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        for h in range(1, 27):
            cnts = [0 for _ in range(26)]
            i = 0
            j = 0
            unique = 0
            noLessThanK = 0
            while j < len(s):
                if unique <= h:
                    idx = ord(s[j]) - ord('a')
                    if cnts[idx] == 0:
                        unique += 1
                    cnts[idx] += 1
                    if cnts[idx] == k:
                        noLessThanK += 1
                    j += 1
                else:
                    idx = ord(s[i]) - ord('a')
                    if cnts[idx] == k:
                        noLessThanK -= 1
                    cnts[idx] -= 1
                    if cnts[idx] == 0:
                        unique -= 1
                    i += 1
                if unique == h and unique == noLessThanK:
                    res = max(j - i, res)
        return res

