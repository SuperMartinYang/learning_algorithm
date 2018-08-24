import collections


class Solution(object):
    def numSimilarGroups1(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # naive way, 2 for loop, O(N^2), TLE
        dic = collections.defaultdict(str)
        visited = [False] * len(A)

        def itis(i, j):
            # true when it can be swap by 2
            one, two = None, None
            for k in range(len(A[i])):
                if A[i][k] == A[j][k]: continue
                if one is None:
                    one = k
                elif two is None:
                    two = k
                else:
                    return False
            if A[i][one] == A[j][two] and A[i][two] == A[j][one]: return True
            return False

        def dfs(i, group):
            if A[i] in dic: return
            dic[A[i]] = A[group]
            visited[i] = True
            for j in range(len(A)):
                if visited[j]: continue
                if itis(i, j):
                    dfs(j, group)
            visited[i] = False

        for i in range(len(A)):
            dfs(i, i)
        return len(set(dic.values()))

    def numSimilarGroups(self, A):

        def itis(x, y):
            return sum(i != j for i, j in zip(x, y)) == 2

        p = {val: val for val in A}
        res = set()

        def find(i):
            while p[i] != i:
                p[i] = p[p[i]]  # shorten the height
                i = p[i]
            return i

        # find connection
        for i in range(len(A)):
            for j in range(i, len(A)):
                if itis(i, j):
                    p[A[j]] = A[i]  # union

        for ss in A:
            ri = find(ss)
            res.add(ri)
        # union

        return len(res)

print(Solution().numSimilarGroups(['tars', 'rats', 'arts', 'star']))