class Solution(object):
    def strobogrammatic_number(self, s):
        """
        86098
        0 1 8 6 9 has this property
        :param s: "86098"
        :return: bool
        """
        k = len(s) / 2
        i = 0
        while i <= k:
            if s[i] != s[len(s) - i - 1]:
                if s[i] == '6' and s[len(s) - i - 1] == '9' or s[i] == '9' and s[len(s) - i - 1] == '6':
                    i += 1
                    continue
                else: return False
            else:
                if s[i] not in "018": return False
                i += 1
        return True
print(Solution().strobogrammatic_number("86098"))