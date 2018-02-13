from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
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

s = Solution()
print s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])