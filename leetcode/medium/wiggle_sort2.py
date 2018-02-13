class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        pivot = self.findKthLargest(nums, len(nums) // 2)
        wiggleTable = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i % 2 == 1:
                wiggleTable[i // 2] = i
            else:
                wiggleTable[- i // 2 - 1] = i
        left = 0
        right = -1

        for i in range(len(nums)):
            if nums[i] > pivot:
                if i % 2 == 0:
                    swap(i, wiggleTable[left])
                left += 1
            elif nums[i] < pivot:
                if i % 2 == 1:
                    swap(i, wiggleTable[right])
                right -= 1
        print(nums)

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

        if k == 0:
            return -1
        return quickselect(0, len(nums) - 1)


s =Solution()
print(s.wiggleSort([1,3,2,2,3,1]))