from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # form graph
        graph = defaultdict(list)
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)

        def getHeight(node):
            # bfs
            queue = [node]
            mask[node] = 1
            level = 0
            while queue:
                flag = False
                tmpQ = []
                for tmp in queue:
                    for nd in graph[tmp]:
                        if mask[nd] == 0:
                            tmpQ.append(nd)
                            mask[nd] = 1
                            flag = True
                level = level + 1 if flag else level
                queue = tmpQ
            return level

        minHeight = float('inf')
        res = []
        for node in range(n):
            mask = [0 for _ in range(n)]
            tmpHeight = getHeight(node)
            if tmpHeight == minHeight:
                res.append(node)
            elif tmpHeight < minHeight:
                res = [node]
                minHeight = tmpHeight
        return res


print(Solution().findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))