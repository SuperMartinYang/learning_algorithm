class Solution(object):
    def form_maximum_rectangle(self, points):
        """
        give several points in axis, find the maximum rectangle can be formed
        :param points: List[point]
        :return: int
        """
        # find two points, which can produce another two points,
        # check whether its in the set
        pset = set(points)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x = [points[i][0], points[j][1]]
                y = [points[j][0], points[i][1]]
                if x in pset and y in pset:
                    res = max(abs(x[0] - y[0]) * abs(x[1] - y[1]))
        return res
