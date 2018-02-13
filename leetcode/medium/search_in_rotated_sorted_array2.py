class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        minEle = min(nums)
        for i in range(len(nums)):
            if nums[i] == minEle:
                minIdx = i
                break
        while abs(minIdx - 1) < len(nums) and nums[minIdx - 1] == minEle:
            minIdx -= 1
        minIdx %= len(nums)

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            realMid = (mid + minIdx) % len(nums)
            if nums[realMid] == target:
                return True
            elif nums[realMid] < target:
                lo = mid + 1
            else:
                hi = mid

        return False

print(Solution().search([1,2,3,4,5,1,1,1], 5))