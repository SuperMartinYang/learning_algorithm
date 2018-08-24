class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = float('-inf')
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    s3 = stack.pop()
                stack.append(nums[i])
        return False