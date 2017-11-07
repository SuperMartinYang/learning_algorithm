class Solution(object):
    def singleNumber(self, nums):
        """
        Given an array of integers, every element appears twice except for one. Find that single one.
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a