class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # backtracking
        res = []
        def helper(ss, idx):
            if ss == t:
                res.append(1)
                return
            for chidx in range(idx, len(s)):
                if s[chidx] == t[len(ss)]:
                    ss += s[chidx]
                    helper(ss, chidx + 1)
                    ss = ss[:-1]
            return
        helper('', 0)
        return sum(res)

    def numDistinct(self, s, t):
        # dp, mm[i][j] means s[0:j] contains t[:i] times, the result is mm[len(t)][len(j)]
        return

s = Solution()
print(s.numDistinct('rrabbbbitrabbit', 'rabbit'))