class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def allDone(d):
            for value in d.values():
                if value > 0:
                    return False
            return True
        if len(s) < len(t):
            return ""
        tDict = {}
        for i in range(len(t)):
            tDict[t[i]] = tDict[t[i]] + 1 if t[i] in tDict else 1
        i = 0
        res = s
        start = 0
        while i < len(s):
            if s[i] in tDict:
                tDict[s[i]] -= 1
                while s[start] in tDict and tDict[s[start]] < 0 or s[start] not in tDict:
                    if s[start] in tDict:
                        tDict[s[start]] += 1
                    start += 1
            i += 1
            if allDone(tDict):
                res = res if len(res) < (i - start) else s[start: i]
        return res if allDone(tDict) else ""

print(Solution().minWindow("ABBBDBACAD","ABD"))