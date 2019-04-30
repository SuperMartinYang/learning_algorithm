import math
class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.seg = [0] * self.getPower2(len(nums))
        self.buildTree(0, len(nums), 0)

    def getPower2(self, n):
        b = int(math.ceil(math.log2(n)))
        return 2 * int(pow(2, b)) - 1
        
    def isPower2(self, n):
        b = int(math.log(n, 2))
        if b ** 2 == n:
            return n
        else:
            return (b + 1) ** 2

    def buildTree(self, lo, hi, pos):
        if lo == hi: self.seg[pos] = self.nums[lo]; return
        mid = (hi + lo) // 2
        self.buildTree(lo, mid, pos * 2 + 1)
        self.buildTree(mid + 1, hi, pos * 2 + 2)
        self.seg[pos] = min(self.seg[pos * 2 + 1], self.seg[pos * 2 + 2])

    def updateTree(self, i, val, pos, lo, hi):
        if i < lo or i > hi: return
        if lo == hi: self.seg[pos] = val; return
        mid = (hi + lo) // 2
        self.updateTree(i, val, pos * 2 + 1, lo, mid)
        self.updateTree(i, val, pos * 2 + 2, mid + 1, hi)
        self.seg[pos] = min(self.seg[pos * 2 + 1], self.seg[pos * 2 + 2])

    def query(self, lo, hi, pos, ql, qh):
        # total overlap, return min(lo, hi)
        if lo <= ql and hi >= qh: return self.seg[pos]
        # not overlap, return max
        if lo > qh or hi < ql: return 1e9
        # partial overlap
        mid = (hi + lo) // 2
        return min(self.query(lo, mid, pos * 2 + 1, ql, qh), self.query(mid + 1, hi, pos * 2 + 2, ql, qh))
