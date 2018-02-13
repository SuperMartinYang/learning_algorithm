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

    def threeSum2(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = len(nums) - 1
            twoSum = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == twoSum:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]: high -= 1
                    high -= 1
                    low += 1
                elif nums[low] + nums[high] < twoSum:
                    low += 1
                else:
                    high -= 1
        return res


s = Solution()
s.threeSum2([0, 0, 0])