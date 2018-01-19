import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        match_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        len_digits = len(digits)
        list_tp = list(match_dict[digits[0]])
        for i in range(1, len_digits):
            products = itertools.product(list_tp, match_dict[digits[i]])
            list_tp = []
            for j in products:
                list_tp.append(j[0] + j[1])
        return list_tp
s = Solution()
print(s.letterCombinations('234'))