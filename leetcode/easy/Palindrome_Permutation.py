import collections
class Solution(object):
    def palindrome_permutation(self, word):
        dic = collections.defaultdict(int)
        for ch in word: dic[ch] += 1
        flag = False
        for key, val in dic.items():
            if val % 2 != 0 and not flag:
                flag = True
            elif val % 2 != 0:
                return False
        return True



print(Solution().palindrome_permutation("abbaa"))