from math import pow, log1p


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary(nums, start, stop):
            if not nums:
                return
            mid = (start + stop) // 2
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[stop - 1]:
                    return binary(nums, mid + 1, stop)
                else:
                    return binary(nums, start, mid)
        return binary(nums, 0, len(nums))



s = Solution()
print s.findMin([4,5,6,7,0,1,2,3])