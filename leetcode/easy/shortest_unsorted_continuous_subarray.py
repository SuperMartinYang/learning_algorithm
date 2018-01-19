class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        new = sorted(nums)
        start = stop = 0
        for i in range(len_nums):
            if new[i] != nums[i]:
                start = i

        for i in range(len_nums - 1, -1, -1):
            if new[i] != nums[i]:
                stop = i

        return start - stop + 1


s = Solution()
print s.findUnsortedSubarray([2,6,4,8,10,9,15])