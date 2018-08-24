class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        cnt = 0
        i = 0
        for j in range(len(S)):
            cnt += 1 if S[j] == '1' else -1
            if cnt == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        res.sort(reverse=True)
        return ''.join(res)


print(Solution().makeLargestSpecial('11011000'))
