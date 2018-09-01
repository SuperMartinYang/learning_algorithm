import collections
class Solution(object):
    def course_schedule(self, cnum, prerequisite):
        graph = collections.defaultdict(list)
        for p, q in prerequisite:
            graph[p].append(q)      # in case, there are multiple prerequisite

        def dfs(cn):
            if visited[cn] == -1: return False
            if visited[cn] == 1: return True
            visited[cn] = -1     # mark as may have conflict
            for pre in graph[cn]:
                if not dfs(pre):
                    return False
            visited[cn] = 1
            return True

        visited = [0] * cnum
        for i in range(cnum):
            if visited[i] == 0:     # haven't visited
                dfs(i)

        return visited.count(True) == cnum

print(Solution().course_schedule(3, [[1, 0], [0, 2]]))