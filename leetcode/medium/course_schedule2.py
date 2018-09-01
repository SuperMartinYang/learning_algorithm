from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # form graph
        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        for c, pc in prerequisites:
            graph[pc].append(c)             # from the prerequisite to the left course
            in_degrees[c] += 1              # in degree == 0, append to visited and res

        # BFS
        visited = [i for i in range(numCourses) if in_degrees[i] == 0]
        res = []
        cnt = 0
        while visited:
            tmp = visited.pop()
            cnt += 1
            res.append(tmp)
            for c in graph[tmp]:
                in_degrees[c] -= 1
                if in_degrees[c] == 0:
                    visited.append(c)
        return res if cnt == numCourses else []


print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))