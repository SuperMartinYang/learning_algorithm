class UnionFind:
    def __init__(self, N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            id[i] = id[id[i]]   # path compression to optimize
            i = id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        id[i] = j

