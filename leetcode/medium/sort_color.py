class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        one_num = two_num = zero_num = 0
        for i in nums:
            if i == 0:
                zero_num += 1
            elif i == 1:
                one_num += 1
            else:
                two_num += 1

        i = 0
        while i < len(nums):
            if zero_num != 0:
                nums[i] = 0
                zero_num -= 1
            elif one_num != 0:
                nums[i] = 1
                one_num -= 1
            elif two_num != 0:
                nums[i] = 2
                two_num -= 1
            i += 1
        return nums

s = Solution()
print(s.sortColors([0]))