class Solution(object):
    def three_sum_smaller(self, nums, target):
        nums = sorted(enumerate(nums), key=lambda x:x[1])
        res = 0
        for i in range(len(nums)):
            s, e = i + 1, len(nums) - 1
            rem = target - nums[i][1]
            while s < e:
                if nums[s][1] + nums[e][1] < rem:
                    res += e - s
                    s += 1
                else:
                    e -= 1
        return res

print(Solution().three_sum_smaller([-2, 0, 1, 3], 2))