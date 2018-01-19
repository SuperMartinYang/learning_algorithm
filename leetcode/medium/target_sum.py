class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dic = {nums[0] : 1, -nums[0] : 1} if nums[0] != 0 else {0 : 2}
        for i in range(1, len(nums)):
            next_dic = {}
            for key in dic:
                if key + nums[i] in next_dic:
                    next_dic[key + nums[i]] += 1
                else:
                    next_dic[key + nums[i]] = 1
                if key - nums[i] in next_dic:
                    next_dic[key - nums[i]] += 1
                else:
                    next_dic[key - nums[i]] = 1
            dic = next_dic
        return dic[S] if S in dic else 0

s = Solution()
print s.findTargetSumWays([1,1,1,1,1], 3)