import heapq
class Solution(object):
    def meeting_rooms_ii(self, intervals):
        """
        find the minimum conference room needed, un-overlap interval can be in one room
        :param intervals: List[time_slots]
        :return: int
        """
        # Solution1: use TreeMap
        # put intervals into TreeMap, key-> intervals.start, val->intervals.end, use floor to find

        # Solution2: heap
        intervals.sort()
        hp = []
        for inter in intervals:
            if hp and hp[0] < inter[0]: heapq.heappop(hp)
            heapq.heappush(hp, inter[1])
        return len(hp)

print(Solution().meeting_rooms_ii([[0, 30],[5, 10],[15, 20]]))