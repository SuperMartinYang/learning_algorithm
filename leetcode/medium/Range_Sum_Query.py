class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(nums)
        self.cache = []
        s = 0
        for i in nums:
            s += i
            self.cache.append(s)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        dif = val - self.nums[i]
        for i in range(i, self.length):
            self.cache[i] += dif

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.cache[j]
        return self.cache[j] - self.cache[i - 1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([7,2,7,2,6])
obj.update(0,2)
obj.update(0,9)
obj.update(3,8)
print obj.sumRange(0,4)