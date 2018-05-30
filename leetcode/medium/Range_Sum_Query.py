class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sumNums = [sum(nums[:j + 1]) for j in range(len(nums))]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        for j in range(i, len(self.nums)):
            self.sumNums[j] = self.sumNums[j] + diff
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sumNums[j]
        return self.sumNums[j] - self.sumNums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray([7,2,7,2,6])
# obj.update(0,2)
# obj.update(0,9)
# obj.update(3,8)
# print(obj.sumRange(0,4))

obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))