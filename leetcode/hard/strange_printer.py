import collections
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        backward, forward = False, True
        tmp = '.' * len(s)

        def getrange(idx, back_forw):
            val = s[idx]
            if back_forw == forward:
                while idx < len(s) and s[idx] == val:
                    idx += 1
            else:
                t = idx
                idx = len(s)
                while idx > t and s[idx - 1] != val:
                    idx -= 1
            return idx

        dp = collections.defaultdict(int)

        def dfs(idx, pre):
            if idx == len(s):
                return 0
            # if idx in dp: return dp[idx]
            for i in range(idx, len(s)):
                if s[i] == pre[i]:
                    continue
                else:
                    # paint to last occurance
                    ep = getrange(i, backward)  # s[ep] != s[i]
                    new = pre[:i] + s[i] * (ep - i) + pre[ep:]
                    if new == s: return 1
                    pall = 1 + dfs(i, new)
                    # paint dif
                    ep = getrange(i, forward)  # s[ep] != s[i]
                    new = pre[:i] + s[i] * (ep - i) + pre[ep:]
                    if new == s: return 1
                    ppart = 1 + dfs(i, new)
                    # dp[i] = min(dp[i] if i in dp else float('inf'), pall, ppart)
                    return min(pall, ppart)
            return -1

        return dfs(0, tmp)

    def strangePrinter(self, s):
        memo = {}
        def dp(i, j):   # memo[i, j] means s[i:j + 1] printer counts
            if (i, j) not in memo:
                ans = 1 + dp(i + 1, j)
                for k in (i + 1, j + 1):
                    if s[i] == s[k]:
                        ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, len(s) - 1)

# print(Solution().strangePrinter("abababac"))
print(Solution().strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"))