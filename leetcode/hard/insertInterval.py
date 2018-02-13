# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        def findIndex(val, start):
            lo, hi = start, len(intervals)
            while lo < hi:
                mid = (hi + lo) // 2
                if intervals[mid].start <= val <= intervals[mid].end:
                    return mid
                elif intervals[mid].start > val:
                    hi = mid
                else:
                    lo = mid + 1
            return -1

        left = findIndex(newInterval.start, 0)
        right = findIndex(newInterval.end, left)
        right = left if right == -1 else right
        res = []
        flag = False
        mergeItem = Interval(intervals[left].start, intervals[right].end if right != left else newInterval.end)
        for i in range(len(intervals)):
            if i < left or i > right:
                res.append(intervals[i])
            else:
                if not flag:
                    res.append(mergeItem)
                    flag = True
        return res
inters = [[1,2],[3,5],[6,7],[8,10],[12,16]]
intervals = []

for i in inters:
    intervals.append(Interval(i[0], i[1]))

newInterval = Interval(4,9)
s = Solution()
print(s.insert(intervals, newInterval))
