class Solution(object):
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {')':'(',
                '}':'{',
                ']':'['}
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(stack) == 0 or stack.pop() != pair[char]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid('{'))