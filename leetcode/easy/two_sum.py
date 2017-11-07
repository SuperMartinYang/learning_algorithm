class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        cur_table = {}
        lenN = len(numbers)
        for i in range(0, lenN):
            if target - numbers[i] in cur_table.keys():
                return [cur_table[target-numbers[i]] + 1, i + 1]
            else:
                cur_table[target-numbers[i]] = i
        return None

a = set()
a.add