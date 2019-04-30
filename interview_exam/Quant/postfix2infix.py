class Solution(object):
    def post2in(self, s):
        expressStack = []
        priority = {'-': 0,
                    '+': 0,
                    '*': 1,
                    '/': 1,
                    '^': 2
                    }
        for i in range(len(s)):
            if s[i].isalnum():
                expressStack.append([s[i], -1])
            else:
                op2 = '(' + expressStack[-1][0] + ')' if priority[s[i]] > expressStack[-1][1] and len(expressStack[-1][0]) > 1 else expressStack[-1][0]
                op1 = '(' + expressStack[-2][0] + ')' if priority[s[i]] > expressStack[-2][1] and len(expressStack[-2][0]) > 1 else expressStack[-2][0]
                expressStack.pop()
                expressStack.pop()
                expressStack.append([op1 + s[i] + op2, priority[s[i]]])
        return expressStack[0][0]

print(Solution().post2in("23*21-/345+*+"))

