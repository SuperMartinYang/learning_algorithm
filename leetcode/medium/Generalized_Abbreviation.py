class Solution(object):
    def generalized_abbreviation(self, s):
        """
        get the abbreviation for s
        :param s: str
        :return: List
        """
        res = []
        # get the str of len
        n = 2 ** len(s)
        for i in range(n):
            # abbreviation is corresponding with the bit represent of changed char, 1-> change, 0-> remain
            tmp = ''
            ps = len(s)
            while i > 0:
                cnt = 0
                if i & 1 == 1:
                    while i & 1 == 1:
                        ps -= 1
                        cnt += 1
                        i >>= 1
                    tmp = str(cnt) + tmp
                else:
                    tmp = s[ps - 1] + tmp
                    ps -= 1
                    i >>= 1
            res.append(s[:ps] + tmp)
        return res

print(Solution().generalized_abbreviation("word"))