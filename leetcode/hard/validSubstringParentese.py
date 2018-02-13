class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = [0 for _ in range(len(s))]
        curMax = 0
        for i in range(len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    longest[i] = longest[i - 2] + 2
                elif s[i - 1] == ')' and s[i - 1 - longest[i - 1]] == '(':
                    longest[i] = longest[i - 1] + 2 + longest[i - 1 - longest[i - 1] - 1]
                curMax = max(longest[i], curMax)
        return curMax

