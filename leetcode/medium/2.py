"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
nums = [2, 7, 11, 15]
target = 9
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup_table = {}
        for i,v in enumerate(nums):     # enumerate : index-value
            if target - v in lookup_table:      # key in dictionary
                return [lookup_table[target-v],i]
            else:
                lookup_table[v] = i
a = Solution()
print(a.twoSum(nums,target))