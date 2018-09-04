import collections
class Solution(object):
    def alien_dictionary(self, words):
        #TODO
        graph = collections.defaultdict(list)
        chset = set()
        res = ''
        indg = [0] * 256
        # all char
        for w in words:
            for ch in w: chset.add(ch)
        # form graph
        for i in range(len(words) - 1):
            mn = min(len(words[i]), len(words[i + 1]))
            j = 0
            while j < mn:
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    break
                j += 1
            if j == mn and len(words[i]) > len(words[i + 1]):
                return ''
        # in degree for node
        for lt in graph.values():
            for val in lt:
                indg[ord(val)] += 1
        # get start node
        level = []
        for ch in chset:
            if indg[ord(ch)] == 0:   # start point
                level.append(ch)
                res += ch
        while level:
            c = level.pop()
            if c in graph:
                for v in graph[c]:
                    indg[ord(v)] -= 1
                    if indg[ord(v)] == 0:
                        level.append(v)
                        res += v
        return res if len(res) == len(chset) else ''


print(Solution().alien_dictionary(["wrt","wrf","er","ett","rftt"]))