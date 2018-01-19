class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        heightList = []
        for node in range(n):
            childset = [node]
            level = 0
            visited = [False for _ in range(n)]
            while childset:
                tmpset = set()
                level += 1
                for childNode in childset:
                    visited[childNode] = True
                    for edge in edges:
                        if childNode in edge:
                            otherNode = edge[0] if edge[0] != childNode else edge[1]
                            if not visited[otherNode]:
                                tmpset.add(otherNode)
                childset = list(tmpset)
            heightList.append([level, node])
        heightList.sort()
        res = []
        minHeight = heightList[0][0]
        k = 0
        while k < len(heightList) and heightList[k][0] == minHeight:
            res.append(heightList[k][1])
            k += 1
        return res

s = Solution()
print s.findMinHeightTrees(2,[[0,1]])