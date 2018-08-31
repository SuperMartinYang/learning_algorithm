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

        # find the reverse point
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

    def nextPermutation2(self, nums):
        # find the decrease point from backward to forward
        decreasePoint = - 1
        for i in range(len(nums) - 1)[::-1]:
            if nums[i] < nums[i + 1]:
                decreasePoint = i
                break
        if decreasePoint == -1: return nums[::-1]
        # find the new higher point
        for i in range(decreasePoint + 1, len(nums)):
            if i == len(nums) - 1 or nums[i + 1] < nums[decreasePoint]:
                nums[decreasePoint], nums[i] = nums[i], nums[decreasePoint]
                print(i)
                break
        # reverse from decrease point (exclude) to the end
        nums = nums[:decreasePoint + 1] + nums[:decreasePoint:-1]
        return nums
s = Solution()
print(s.nextPermutation2([1,3,4,6,5,2]))
