from collections import defaultdict
import heapq


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        # key is the start point, value is idx
        start_hash = defaultdict(list)
        # key is the end point, value is idx
        end_hash = defaultdict(list)
        for i in range(len(intervals)):
            heapq.heappush(start_hash[intervals[i].start], i)
            heapq.heappush(end_hash[intervals[i].end], i)
        res = [-1 for _ in intervals]
        for i in range(len(res)):
            for key in sorted(start_hash.keys()):
                if intervals[i].end <= key and res[i] == -1:
                    res[i] = start_hash[key][0]
        return res


print(Solution().findRightInterval([Interval(4, 5), Interval(2, 3), Interval(1, 2)]))
