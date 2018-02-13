class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValid(subS):
            left = 0
            for ch in subS:
                if ch == '(':
                    left += 1
                else:
                    left -= 1
            return left == 0
        lenLevel = len(s)
        if isValid(s):
            return lenLevel
        waitList = [s]
        while waitList:
            tmpList = []
            lenLevel -= 1
            for ss in waitList:
                for i in range(len(ss)):
                    waitS = ss[:i] + ss[i + 1:]
                    if isValid(waitS):
                        return lenLevel
                    tmpList.append(waitS)
            waitList = tmpList
        return 0