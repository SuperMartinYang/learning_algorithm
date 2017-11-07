class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            pre = self.countAndSay(n-1)
            cur = pre[0]
            tot = 1
            result = ''
            for j in range(1,len(pre)):
                if pre[j] == cur:
                    tot += 1
                else:
                    result += str(tot) + cur
                    cur = pre[j]
                    tot = 1

            result += str(tot) + cur
            return result


s = Solution()
print(s.countAndSay(4))