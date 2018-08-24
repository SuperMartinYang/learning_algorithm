class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.bt(res, s, 0, [])
        return res

    def bt(self, res, s, idx, tmp):
        if len(tmp) == 4 and idx == len(s):
            ss = '.'.join(tmp)
            res.append(ss)
            return
        if len(tmp) == 4:
            return
        for j in range(idx + 1, len(s) if idx + 4 >= len(s) else idx + 4):
            sub = s[idx:j]
            if 0 <= int(sub) <= 255:
                tmp.append(sub)
                self.bt(res, s, j, tmp)
                tmp.pop()

print(Solution().restoreIpAddresses('25525511135'))
