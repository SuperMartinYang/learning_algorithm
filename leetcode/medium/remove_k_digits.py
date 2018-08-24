class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return num
        minNum = '9' * (len(num) - k)
        i = 0
        while i < len(num):
            if i == 0:
                tmp = i
                while num[tmp + 1] == '0':
                    tmp += 1
                tmpMin = self.removeKdigits(num[tmp + 1:], k - 1)
            else:
                tmpMin = self.removeKdigits(num[:i] + num[i + 1:], k - 1)
            if len(tmpMin) < len(minNum):
                minNum = tmpMin
            elif len(tmpMin) == len(minNum):
                minNum = min(minNum, tmpMin)
            i += 1
        return minNum


print(Solution().removeKdigits("10200", 1))