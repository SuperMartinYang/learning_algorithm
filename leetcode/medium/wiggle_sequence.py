class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        nearly the same as linear house rob
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        f = 1
        d = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                f = d + 1
            elif nums[i] < nums[i - 1]:
                d = f + 1
        return max(f, d)

    def wiggleMaxLength2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        dp = [None for _ in range(len(nums))]
        dp[0] = [1, None]
        # longest = 0
        for i in range(1, len(nums)):
            for j in range(i - 1, - 1, -1):
                dif = '>' if nums[i] - nums[j] > 0 else '=' if nums[i] - nums[j] == 0 else '<'
                if dif == '=' or dif == dp[j][1]:
                    if not dp[i]:
                        dp[i] = dp[j]
                    continue
                elif not dp[i] or (dp[i] and dp[i][0] < 1 + dp[j][0]):
                    dp[i] = [1 + dp[j][0], dif]
        return max(dp)[0]


print(Solution().wiggleMaxLength2([1,17,5,10,13,15,10,5,16,8]))