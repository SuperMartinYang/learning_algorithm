class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] > nums[hi]:
                lo = mid
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                while mid < hi and nums[mid] == nums[hi]:
                    hi -= 1
        if nums[lo] <= nums[lo - 1] and nums[lo] <= nums[(lo + 1) % len(nums)]: return nums[lo]
        if nums[hi] <= nums[hi - 1] and nums[hi] <= nums[(hi + 1) % len(nums)]: return nums[hi]


print(Solution().findMin([3,1,1]))


