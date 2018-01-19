class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        len_nums = len(nums)

        m, l = [], []
        m.append(nums[0])  # max = [max_1, max_2... max_n]
        l.append(nums[0])  # little = [little_1, little_2... little_n]     most small(negative) might * negative -> greatest
        res = nums[0]

        for i in range(1, len_nums):
            m.append(max(max(m[i - 1] * nums[i], l[i - 1] * nums[i]), nums[i]))
            l.append(min(min(m[i - 1] * nums[i], l[i - 1] * nums[i]), nums[i]))
            res = max(res, m[i])

        return res

s = Solution()
print(s.maxProduct([-4, -3]))
