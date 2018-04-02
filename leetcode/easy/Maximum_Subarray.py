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

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (0 if dp[i -1] < 0 else dp[i - 1])
            res = max(dp[i], res)
        return res

s = Solution()
print(s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))