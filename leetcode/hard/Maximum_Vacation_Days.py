class Solution(object):
    def maximum_vacation_days(self, flights, days, N, K):
        """

        :param flights: 2-D List[List]
        :param days: 2-D List[List]
        :param N: N cities
        :param K: K weeks
        :return: int
        """
        if not flights: return 0
        res = []
        for i in range(N):
            helper(flights, days, i if flights[0][i] else 0, 0, 0, N, K)
        return min(res)

    def helper(self, flights, days, flight, week, tmp, N, K):
        # TODO
        if week == K:
            res.append(tmp)
        tmp += days[flight][week]
        return