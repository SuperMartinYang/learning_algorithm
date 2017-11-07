class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hash_table = {}
        result = []
        len_ = len(nums)
        if len_ == 0:
            return None
        if len_ == 1:
            if nums[0] == 0:
                return nums
            else:
                return None
        for i in range(len_):
            for j in range(len_-1, i, -1):
                if 0 - nums[i] in hash_table.keys():
                    result.append(hash_table[0-nums[i]].append(nums[i]))
                elif 0 - nums[j] in hash_table.keys():
                    result.append(hash_table[0-nums[j]].append(nums[j]))
                else:
                    hash_table[nums[j] + nums[i]] = [nums[j],nums[i]]
        # result = set(result)
        # result = list(result)
        # for i in range(len(result)):
        #     result[i] = list(result[i])
        return result

s = Solution()
s.threeSum([-1,0,1,2,-1,-4])