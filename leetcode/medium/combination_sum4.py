class Solution(object):
    _res = 0

    def combinationSum4(self, nums, target):
        """
        backtracking TLE
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.helper(nums, target)
        return self._res

    def helper(self, nums, rem):
        if rem == 0:
            self._res += 1
            return
        for num in nums:
            rem -= num
            if rem >= 0:
                self.helper(nums, rem)
            rem += num

    def combinationSum42(self, nums, target):
        """
        Dynamic Programming
        dp[i] = ways to form i using nums
        :param nums:
        :param target:
        :return:
        """
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] = dp[i - nums[j]] + dp[i]
        return dp[target]

print(Solution().combinationSum42([4,2,1], 32))
