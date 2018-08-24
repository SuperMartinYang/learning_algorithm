class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    res.add(nums[i])
                    break
                else:
                    tmp = nums[i]
                    nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]
        return list(res)


print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))