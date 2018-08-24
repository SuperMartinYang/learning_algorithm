import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = lo = hi = 0
        counts = collections.Counter()
        while hi < len(s):
            counts[s[hi]] += 1
            max_char_n = counts.most_common(1)[0][1]
            while hi - lo + 1 - max_char_n > k:
                counts[s[lo]] -= 1
                lo += 1
            res = max(res, hi - lo + 1)
            hi += 1
        return res



# print(Solution().characterReplacement('ABAB', 2))
print(Solution().characterReplacement('AABABAA', 1))