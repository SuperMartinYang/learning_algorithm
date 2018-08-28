import collections
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        """
        ["great","acting","skills"]
        ["fine","drama","talent"]
        [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
        """
        # DFS
        if len(words1) != len(words2): return False
        dic = collections.defaultdict(list)
        for p, q in pairs:
            dic[p].append(q)
            dic[q].append(p)

        def dfs(start, end, visited):
            visited.add(start)
            for item in dic[start]:
                if item in visited: continue
                if item == end:
                    return True
                else:
                    if dfs(item, end, visited): return True
            return False

        for i in range(len(words1)):
            visited = set() # remember whether we have already visited this word
            if words1[i] != words2[i] and not dfs(words1[i], words2[i], visited):
                return False
        return True
        # union-find

print(Solution().areSentencesSimilarTwo(["great","acting","skills"],["fine","drama","talent"], [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]))