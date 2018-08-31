class Solution(object):
    def meeting_rooms(self, intervals):
        """
        [meet_time_slots]
        check whether there's overlap
        :return: bool
        """
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
