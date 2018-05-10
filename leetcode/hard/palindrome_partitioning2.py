class Solution(object):
    def minCut(self, s):
        """
        2 DP, cuts[0] is the answer
        cuts[i] means cuts from i to n-1
        :type s: str
        :rtype: int
        """
        pal = [[False for _ in range(len(s))] for _ in range(len(s))]
        cuts = [len(s) - i - 1 for _ in range(len(s))]
        for start in range(len(s) - 1, -1, -1):
            for stop in range(start, len(s)):
                if s[start] == s[stop] and (stop - start < 2 or pal[start + 1][stop - 1]):
                    pal[start][stop] = True
                    if stop == len(s) - 1:
                        cuts[start] = 0
                    else:
                        cuts[start] = min(cuts[start], 1 + cuts[stop + 1])
        return cuts[0]

print(Solution().minCut("aabasdciii"))
# print(isPa('abca'))