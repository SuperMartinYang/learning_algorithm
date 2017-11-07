class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = None
        stop1 = stop2 = 0
        max_ = 0
        len_ = len(nums)
        for i in range(len_ -1):
            if nums[i] >= nums[i+1] and start == None:
                start = i
                if nums[i] > max_:
                    max_ = nums[i]
                stop1 = i+1
            elif nums[i] > nums[i+1] and start != None:
                stop1 = i+1
            else:
                if nums[i] >= max_:
                    max_ = nums[i]
                    stop2 = i
        if start == None:
            return 0
        if nums[len_-1] < max_:
            stop1 = len_ - 1
            return stop1 - start + 1
        else:
            stop2 = len_ - 1
            if stop2 == len_ -1:
                return stop1- start + 1
            else:
                return stop2 - start + 1

s = Solution()
a = []
a.sort()
a = s.findUnsortedSubarray([2,6,4,8,10,11,10])
print(a)