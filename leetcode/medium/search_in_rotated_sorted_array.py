class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the pivot
        if nums == []:
            return -1
        start = 0
        stop = len(nums) - 1
        while start < stop:
            mid = (start + stop) // 2
            if nums[mid] < nums[stop]:
                stop = mid
            else:
                start = mid + 1
        # so pivot is start
        pivot = start
        # real index is (now_index - pivot) % len(nums)
        start, stop = 0, len(nums) - 1
        while start <= stop:
            mid = (start + stop) // 2
            real_mid = (mid + pivot) % len(nums)
            if nums[real_mid] > target:
                stop = mid - 1
            elif nums[real_mid] < target:
                start = mid + 1
            else:
                return real_mid
        return -1


s = Solution()
print s.search([4], 2)