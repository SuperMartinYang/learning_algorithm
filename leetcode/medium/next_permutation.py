class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, point):
            for i in range(point, int((point + len(nums)) / 2)):
                swap(nums, i, len(nums) + point - i - 1)

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        reverse_point = 0

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                reverse_point = i
                break
        reverse(nums, reverse_point)
        if reverse_point != 0:
            for i in range(reverse_point, len(nums)):
                if nums[i] > nums[reverse_point - 1]:
                    swap_point = i
                    break
            swap(nums, swap_point, reverse_point - 1)
        return nums

s = Solution()
print(s.nextPermutation([1,3,2]))