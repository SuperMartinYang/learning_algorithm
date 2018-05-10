class Solution(object):
    def isScramble(self, s1, s2, reverse=False):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        point = 1
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if len(s1) == 2:
            return s1[::-1] == s2

        arr1 = [0 for i in range(128)]
        arr2 = [0 for i in range(128)]
        for i in range(len(s1)):
            arr1[ord(s1[i])] += 1
            arr2[ord(s2[i])] += 1
            if arr1 == arr2:
                point = i + 1
                break
        # if point == len(s1):
        #     return False
        return (False if point == len(s1) else (self.isScramble(s1[:point], s2[:point]) and self.isScramble(s1[point:], s2[point:]))) or (False if reverse else self.isScramble(s1[::-1], s2, True))

print(Solution().isScramble('bba', 'abb'))
# print(Solution().isScramble('great', 'rgeat'))
# print(Solution().isScramble('abcde', 'caebd'))