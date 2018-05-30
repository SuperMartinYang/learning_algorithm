class Solution(object):
    def wiggleSort(self, nums):
        """
        O(n) time
        O(n) space
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

    def findKthEle(self, nums, k):
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
            if big == k:
                return pivot
            elif big < k:
                return quickselect(big + 1, end)
            else:
                return quickselect(start, big - 1)

        if k == 0:
            return -1
        return quickselect(0, len(nums) - 1)

    def wiggleSort2(self, nums):
        """
        O(n log n) time
        O(n) space
        :param nums:
        :return:
        """
        tmp = sorted(nums)
        k = (len(nums) + 1) // 2
        n = len(nums)
        for i in range(len(nums)):
            if i & 1 == 0:
                nums[i] = tmp[k]
                k -= 1
            else:
                nums[i] = tmp[n]
                n -= 1

    def wiggleSort3(self, nums):
        """
        Virtual indexing
        3-way partitioning
        O(n) time
        O(1) space
        :param nums:
        :return:
        """
        # func A for virtual index
        n = len(nums)
        i, j, k = 0, 0, n - 1

        def A(idx):     # make idx 0, 1, 2, 3, 4..., 2n -> 1, 3, 5, 7, 9 ... 2n -1, 0, 2, 4, 6, 8, ... 2n
            return (1 + 2 * idx) % (n | 1)

        def swap(idx1, idx2):
            tmp = nums[idx1]
            nums[idx1] = nums[idx2]
            nums[idx2] = tmp

        mid = n // 2
        mid_ele = self.findKthEle(nums, mid)
        while j <= k:
            if nums[A(j)] > mid_ele:
                swap(A(i), A(j))
                i += 1
                j += 1
            elif nums[A(j)] < mid:
                swap(A(j), A(k))
                k -= 1
            else:
                j += 1
        return nums

s =Solution()
print(s.wiggleSort3([1,3,2,2,3,1]))