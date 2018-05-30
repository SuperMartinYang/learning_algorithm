from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        bfs wrong
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flyDict = defaultdict(list)
        mask = {}
        for ticket in tickets:
            flyDict[ticket[0]].append(ticket[1])
            mask[ticket[0]] = False
            mask[ticket[1]] = False
        start = ['JFK']
        res = []
        while start:
            for p in start:
                if mask[p]:
                    continue
                res.append(p)
                mask[p] = True
                start = sorted(flyDict[p])
                break
        return res

    def findItinerary2(self, tickets):
        """
        DFS works, easy understand
        :param tickets:
        :return:
        """
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []

        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            route.append(airport)

        dfs('JFK')
        return route[::-1]

s = Solution()
print(s.findItinerary2([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))