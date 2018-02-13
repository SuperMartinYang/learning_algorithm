class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = 0
        while i < len(nums):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1)
            i + 1
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                return i + 1
        return i + 1

s = Solution()
print(s.firstMissingPositive([3]))