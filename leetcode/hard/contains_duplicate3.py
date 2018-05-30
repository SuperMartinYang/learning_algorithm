class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        brute force
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # if k > len(nums):
            # return False
        for i in range(len(nums)):
            for j in range(i + 1, i + k + 1):
                if j >= len(nums):
                    break
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        """
        bucket
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if t < 0: return False
        bucket = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w
            if m in bucket:
                return True
            if m - 1 in bucket and abs(bucket[m - 1] - nums[i]) < w:
                return True
            if m + 1 in bucket and abs(bucket[m + 1] - nums[i]) < w:
                return True
            bucket[m] = nums[i]
            if i >= k: del bucket[nums[i - k] // w]
        return False