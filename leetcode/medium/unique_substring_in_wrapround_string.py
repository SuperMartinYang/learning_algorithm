class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        in_it = set()
        i = 0
        while i < len(p):
            j = i
            while j < len(p):
                if j == i or (ord(p[j]) - ord(p[j - 1]) == 1) or (ord(p[j]) - ord(p[j - 1]) == -25 and p[j - 1] == 'z'):
                    in_it.add(p[i:j + 1])
                    j += 1
                else:
                    break
            i += 1
        return len(in_it)


print(Solution().findSubstringInWraproundString('zab'))