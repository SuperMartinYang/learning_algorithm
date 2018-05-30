class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        nums.sort()
        # dp[i] means from 0 - i there are dp[i] divisible number for nums[i]
        dp = [1 for _ in range(len(nums))]
        res = []
        parent = [-1 for _ in range(len(nums))]
        for j in range(1, len(nums)):
            for i in range(j - 1, -1, -1):
                if nums[j] % nums[i] == 0 and dp[i] + 1 > dp[j]:
                    dp[j] = 1 + dp[i]
                    parent[j] = i
        largestAt = dp.index(max(dp))
        # restore
        while parent[largestAt] > -1:
            res.append(nums[largestAt])
            largestAt = parent[largestAt]
        res.append(nums[largestAt])
        return res


print(Solution().largestDivisibleSubset([1,2,3]))