class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if i == (len(nums) - 1):
                if target <= nums[i]:
                    return i
                return len(nums)
            if target > nums[i] and target < nums[i + 1]:
                return i + 1
            elif target <= nums[i]:
                return i

s = Solution()
print(s.searchInsert([1],0))