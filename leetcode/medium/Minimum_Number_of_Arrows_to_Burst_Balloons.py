class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort()
        cnt = 1
        shrink_range = [points[0][0], points[0][1]]
        for i in range(1, len(points)):
            if points[i][0] <= shrink_range[1]:
                shrink_range[0] = points[i][0]
                if points[i][1] <= shrink_range[1]:
                    shrink_range[1] = points[i][1]
            else:
                cnt += 1
                shrink_range = points[i]
        return cnt