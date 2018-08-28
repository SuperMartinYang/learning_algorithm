class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # recursive way to solve this problem
        # 1. preSum
        # 2. helper function to calculate the smallest dif
        sm = 0
        preS = [0]
        for n in nums:
            sm += n
            preS.append(sm)
        vd = {}     # visited[(i, m)] dic to memoization the smallest sum from i and has m split available
        def helper(idx, m):
            if m == 1: return preS[-1] - preS[idx]
            if idx >= len(preS) - 1: return float('inf')
            if len(preS[idx + 1:]) <= m: return max(nums[idx:]) if idx < len(nums) else float('inf')
            if (idx, m) in vd: return vd[idx, m]
            res = float('inf')
            for i in range(idx + 1, len(preS)):
                res = min(res, max(preS[i] - preS[idx], helper(i, m - 1)))
            vd[idx, m] = res
            return res
        return helper(0, m)


print(Solution().splitArray([2,3,1,2,4,3], 5))