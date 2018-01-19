class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= nums[mid - 1] and nums[mid] >= nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            elif nums[mid] < nums[mid - 1]:
                hi = mid
        return lo

s = Solution()
print s.findPeakElement([1,2])