class Solution(object):
    def __init__(self, nums):
        """

        :param nums: List[List]
        """
        self.nums = nums
        self.m = len(nums)
        self.n = len(nums[0]) if self.m else 0
        self.mat = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        self.bit = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        # init
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, nums[i][j])
        print(self.mat)

    def update(self, i, j, val):
        dif = val - self.mat[i + 1][j + 1]
        x = i + 1
        while x < self.m + 1:
            y = j + 1
            while y < self.n + 1:
                # update
                self.bit[x][y] += dif
                y += y & -y
            x += x & -x
        self.mat[i + 1][j + 1] = val
    def getSum(self, i, j):
        res = 0
        x = i
        while x > 0:
            y = j
            while y > 0:
                res += self.bit[x][y]
                y -= y & -y
            x -= x & -x
        return res

    def rangeSum(self, i, j, x, y):
        return self.getSum(x + 1, y + 1) - self.getSum(x + 1, j) - self.getSum(i, y + 1) + self.getSum(i, j)

s = Solution([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
print(s.rangeSum(2, 1, 4, 3))
s.update(3,2,2)
print(s.rangeSum(2, 1, 4, 3))


