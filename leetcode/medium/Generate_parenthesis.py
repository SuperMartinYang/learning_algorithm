class Solution(object):
    def generateParenthesis(self, n):
        """
        n   '('
        n-1 '(' it is required to follow by n-1 ')' and do the remaining things by call generateparenthesis recursively
        n-2 '('

        then,

        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        s = ''
        result = []
        for i in range (n):
            l1 = self.generateParenthesis(i)
            l2 = self.generateParenthesis(n-i-1)
            for x in l1:
                s = '(' + x + ')'
                s1 = ''
                for y in l2:
                    s1 =  s + y
                    result.append(s1)
        return result
s = Solution()

print(s.generateParenthesis(3))