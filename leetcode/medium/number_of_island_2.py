class UnionFind(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.root = [-1] * (m * n)
        self.rank = [0] * (m * n)


    def union(self, x, y):
        rootx = self.find(x[0] * self.n + x[0])
        rooty = self.find(y[0] * self.n + y[0])
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.rank[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.rank[rootx] = rooty
            else:
                self.rank[rootx] = rooty
                self.rank[rooty] += 1

    def find(self, idx):
        if self.root[idx] != idx:
            self.root[idx] = self.find(self.root[idx])
        return self.root[idx]

    def add(self, x):
        idx = x[0] * self.n + x[1]
        self.root[idx] = idx

class Solution(object):
    def number_of_island_2(self, m, n, position):
        uf = UnionFind(m, n)
        res = [0]
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for p in position:
            flag = False
            uf.add(p)
            for i, j in d:
                x = p[0] + i
                y = p[1] + j
                if 0 <= x < m and 0 <= y < n and uf.root[x * n + y] != -1:
                    uf.union(p, [x, y])
                    flag = True
            res.append(res[-1] + 1 if not flag else res[-1])
            print(uf.root)
        return res[1:]

print(Solution().number_of_island_2(3, 3, [[0,0], [0,1], [1,2], [2,1]]))