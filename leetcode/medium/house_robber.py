class Solution(object):
    def rob1(self, nums):
        """
        line
        :param nums:
        :return:
        """
        r, nr = 0, 0
        for i in range(len(nums)):
            tmp = nr
            nr = max(r, nr)
            r = tmp + nums[i]
        return max(r, nr)


    def rob2(self, nums):
        """
        circle
        :type nums: List[int]
        :rtype: int
        """
        #convert to a line
        def helper(start, stop):
            r, nr = 0, 0
            for i in range(start, stop):
                tmp = nr
                nr = max(r, nr)
                r = tmp + nums[i]
            return max(r, nr)
        # rob 0 / 1
        if len(nums) == 1:
            return nums[0]
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))