class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def quickselect(start, end):
            pivot = nums[end]
            small, big = start, start
            while small < end:
                if nums[small] <= pivot:
                    swap(big, small)
                    big += 1
                small += 1
            swap(big, end)
            if big == len(nums) - k:
                return pivot
            elif big < len(nums) - k:
                return quickselect(big + 1, end)
            else:
                return quickselect(start, big - 1)

        return quickselect(0, len(nums) - 1)

s = Solution()
print(s.findKthLargest([1,2,5,6,4,3], 2))