class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {0: [[]]}
        nums.sort()
        for i in range(1, len(nums) + 1):
            key = i - 1
            for k in range(len(dic[key])):
                if i not in dic:
                    dic[i] = []
                for j in range(len(nums)):
                    sub = dic[key][k]
                    if key == 0:
                        dic[i].append(sub + [nums[j]])
                    elif nums[j] > dic[key][k][-1]:
                        dic[i].append(sub + [nums[j]])
        result = []
        for key in dic:
            result.extend(i for i in dic[key])
        return result

s = Solution()
print s.subsets([1,2,3,4])