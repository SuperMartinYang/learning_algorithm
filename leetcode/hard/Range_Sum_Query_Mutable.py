class Solution(object):
    def __init__(self, nums):
        """
        # TODO memo
        :param nums: List[int]
        """
        self.nums = nums
        self.num = [0] * (len(nums) + 1)    # store recent state
        self.bit = [0] * (len(nums) + 1)    # binary index tree
        for i in range(len(nums)):          # init recent state using update
            # update ele in i + 1
            self.update(i, nums[i])
        print(self.bit)

    def rangeSum(self, i, j):               # get the rangeSum
        return self.getSum(j + 1) - self.getSum(i)

    def update(self, i, val):               # when ele in idx i changed to val 
        dif = val - self.num[i + 1]
        j = i + 1
        while j < len(self.num):
            self.bit[j] += dif
            j += j & -j
        self.num[i + 1] = val

    def getSum(self, i):                    # get the sum from [0, i-1] in ori arr, [0, i] in recent state
        j = i
        res = 0
        while j > 0:
            res += self.bit[j]
            j -= j & -j
        return res


print(Solution([1,3,5]).rangeSum(0, 2))