class BinaryIndexTree:
    def __init__(self, nums):
        self.n = len(nums) + 1
        self.preNum = [0] * self.n
        self.bit = [0] * self.n
        for idx, val in enumerate(nums):
            self.update(idx, val)

    def update(self, idx, val):
        dif = val - self.preNum[idx + 1]
        j = idx + 1
        while j < self.n:
            self.bit[j] += dif
            j += j & -j
        self.preNum[idx + 1] += dif

    def rangeSum(self, i, j):
        return self.getSum(j + 1) - self.getSum(i)

    def getSum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res