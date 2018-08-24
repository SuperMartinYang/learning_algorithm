# Definition for an interval.;
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        res = 0
        intervals.sort(key=lambda x: x.end)
        tmp = float('-inf')
        for i in range(len(intervals)):
            if tmp > intervals[i].start:
                res += 1
            else:
                tmp = intervals[i].end
        return res
