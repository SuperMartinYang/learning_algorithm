class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(ss):
            res = ''
            i = 0
            length = 0
            stack = []
            num = 0
            sign = '+'
            while i < len(ss):
                if ss[i].isdigit():
                    num = num * 10 + ord(ss[i]) - ord('0')
                if ss[i] == ')':
                    if num:
                        stack.append(num if sign == '+' else -num)
                    return [sum(stack), length + 1]
                elif i < len(ss) and ss[i] != ')' and not ss[i].isdigit() and ss[i] != ' ' and ss[i] != '(' or i == len(ss) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    sign = ss[i]
                    num = 0
                elif ss[i] == '(':
                    tmp = helper(ss[i + 1:])
                    if sign == "+":
                        stack.append(tmp[0])
                    elif sign == '-':
                        stack.append(-tmp[0])
                    i += tmp[1]
                    length = i
                    while i < len(ss) and ss[i] == ' ':
                        i += 1
                        length += 1
                    sign = ss[i] if i < len(ss) else '+'
                i += 1
                length += 1
            return [sum(stack), length]
        return helper(s)[0]

print(Solution().calculate("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"))
print(Solution().calculate("2147483647"))
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))