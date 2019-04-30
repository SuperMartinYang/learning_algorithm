class Solution(object):

    def pre2in(self, s):
        expressStack = []
        priority = {'-': 0,
                    '+': 0,
                    '*': 1,
                    '/': 1,
                    '^': 2
                    }
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                expressStack.append([s[i], -1])
            else:
                op1 = '(' + expressStack[-1][0] + ')' if priority[s[i]] > expressStack[-1][1] and len(expressStack[-1][0]) > 1 else expressStack[-1][0]
                op2 = '(' + expressStack[-2][0] + ')' if priority[s[i]] > expressStack[-2][1] and len(expressStack[-2][0]) > 1 else expressStack[-2][0]
                expressStack.pop()
                expressStack.pop()
                expressStack.append([op1 + s[i] + op2, priority[s[i]]])
        return expressStack[0][0]

s = Solution()
# print(s.pre2in("+^/*23-212*3-41"))
print(s.pre2in("345+*"))