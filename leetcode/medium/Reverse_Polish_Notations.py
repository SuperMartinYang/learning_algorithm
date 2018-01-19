class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        polish_stack = []
        oper = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in oper:
                polish_stack.append(int(tokens[i]))
            else:
                op2 = polish_stack.pop()
                op1 = polish_stack.pop()
                if tokens[i] == '+':
                    res = op1 + op2
                elif tokens[i] == '-':
                    res = op1 - op2
                elif tokens[i] == '*':
                    res = op1 * op2
                else:
                    res = op1 // op2
                polish_stack.append(res)
        return polish_stack.pop()

s = Solution()
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])