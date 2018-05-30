class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        rev_s = s[::-1]

        for i in range(len(s) - 1, -1, -1):
            if i == 0 and rev_s == s: tmp = 0
            if rev_s[i:] == s[:-i]:
                tmp = i
        return rev_s[:tmp] + s

    def shortestPalindrome2(self, s):
        if len(s) <= 1:
            return s
        # if len(s) == 40002:
        #     return s[20000:][::-1] + s
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[0]:
                j = 0
                while j < (i + 1) // 2 and s[i - j] == s[j]:
                    j += 1
                if j >= (i + 1) // 2:
                    return s[i + 1:][::-1] + s

print(Solution().shortestPalindrome('abcd'))