class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool, false: cycle, true: no cycle
        """
        if numCourses == 0 or prerequisites == []:
            return True
        Adj = [[] for _ in range(numCourses)]
        mask = [0] * numCourses
        for x,y in prerequisites:
            Adj[x].append(y)
        def dfs(i):
            if mask[i] == -1:   # visit a node which is visiting. means a cycle
                return False
            if mask[i] == 1:    # has been visited
                return True
            mask[i] = -1   # is visiting
            for s in Adj[i]:
                if not dfs(s):
                    return False
            mask[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

s = Solution()
print(s.canFinish(2,[[1,0],[0,1]]))