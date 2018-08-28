class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                stack.append(t)
            else:
                oper2 = stack.pop()
                oper1 = stack.pop()
                tmp = str(int(eval(oper1 + t + oper2)))
                stack.append(tmp)
        return int(stack.pop())


print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))