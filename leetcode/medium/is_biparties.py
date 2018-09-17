class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        points = set()
        m = len(graph)
        for i in range(m):
            points.add(i)
            for j in range(len(graph[i])):
                points.add(graph[i][j])

        color = [0] * len(points)

        def dfs(node, clr):
            color[node] = clr
            for n in graph[node]:
                if color[n] == clr or (color[n] == 0 and not dfs(n, -clr)): return False
            return True

        # cuz maybe some node is not all connected together
        for i in range(m):
            # not visited
            if color[i] == 0:
                # start from i, set its color be 1
                if not dfs(i, 1):
                    return False
        return True


print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
