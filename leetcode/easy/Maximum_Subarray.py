class Solution(object):
    def maxSubArray(self, nums):
        """
        For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
        the contiguous subarray [4,-1,2,1] has the largest sum = 6.
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        max_i, max_j = None, None
        i = this_sum = max_sum = 0
        if max(nums) < 0:           # all negative number
            return max(nums)
        for j in range(nums_len):
            this_sum += nums[j]
            if this_sum > max_sum:
                max_sum = this_sum
                max_i = i
                max_j = j
            elif this_sum < 0:        # not else, because even this_sum is smaller than max_sum, but if it is positive, it is also worth to use
                i = j + 1
                this_sum = 0
        return max_sum

s = Solution()
print(s.maxSubArray([-1,2]))