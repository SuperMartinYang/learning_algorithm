class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 1 or n > nums[i - 1]:
                nums[i] = n
                i += 1
        return i

s = Solution()
s.removeDuplicates([1,1,1,2,2,3])