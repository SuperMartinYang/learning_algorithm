class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        wrong = None        # the reason why use None is that wrong is used as index, if no wrong, it should be None, if there is, it should be index, in case of being ambiguous with 0 index
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if wrong is not None:
                    return False
                wrong = i

        return wrong is None or wrong == 0 or wrong == (len(nums) - 2) or nums[wrong - 1] <= nums[wrong + 1] or nums[wrong] <= nums[wrong + 2]      # increasing only valid when A[i-1] < A[i] < A[i + 1]
s = Solution()
print(s.checkPossibility([4,2,1]))