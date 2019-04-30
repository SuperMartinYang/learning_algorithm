class Solution(object):
    def encode(self, strs):
        res = ''
        for s in strs:
            l = len(s)
            res += str(l) + '/' + s
        return res

    def decode(self, s):
        res = []
        i, l = 0, 0
        while i < len(s):
            l = int(s[i])
            res.append(s[i + 2:i + 2 + l])
            i = i + 2 + l
        return res

print(Solution().encode(['hello', 'world']))
print(Solution().decode('6/hel/lo5/world'))