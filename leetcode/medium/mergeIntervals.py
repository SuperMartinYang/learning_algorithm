# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%d, %d]' % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def swap(intervals, i, j):
            tmp = intervals[i]
            intervals[i] = intervals[j]
            intervals[j] = tmp

        def partition(intervals, low, high):
            pivot = intervals[high]
            i = low - 1
            for j in range(low, high):
                if intervals[j].start <= pivot.start:
                    i += 1
                    swap(intervals, i, j)
            swap(intervals, i + 1, high)
            return i + 1

        def quickSortIntervals(intervals, low, high):
            if low < high:
                pi = partition(intervals, low, high)

                quickSortIntervals(intervals, low, pi - 1)
                quickSortIntervals(intervals, pi + 1, high)

        if not intervals:
            return []
        quickSortIntervals(intervals, 0, len(intervals) - 1)
        bot = intervals[0].start
        up = intervals[0].end
        res = []
        i = 1

        while i < len(intervals):
            if intervals[i].start > up:
                res.append(Interval(bot, up))
                bot = intervals[i].start
                up = intervals[i].end
            else:
                if intervals[i].end > up:
                    up = intervals[i].end
            i += 1
        res.append(Interval(bot, up))
        return res

s = Solution()
print s.merge([Interval(1, 4), Interval(0, 4), Interval(3, 18)])[0]