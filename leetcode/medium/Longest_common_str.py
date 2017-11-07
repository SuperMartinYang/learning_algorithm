class Solution:
    def lcs(self, s1, s2):
        '''
        :param self:
        :param s1:  str
        :param s2:  str
        :return:    str
        '''
        if not s1 or not s2:
            return ''
        m, n = len(s1), len(s2)
        if s1[0] == s2[0]:
            return s1[0] + self.lcs(s1[1:], s2[1:])
        else:
            s = self.lcs(s1, s2[1:])
            s_ = self.lcs(s1[1:], s2)
            if len(s) > len(s_):
                return s
            else:
                return s_

s = Solution()
print(s.lcs('eat','sea'))