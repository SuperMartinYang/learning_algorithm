class UnionFind:
    def __init__(self, n):
        self.parent = range(n)
        self.rank = [0] * n

    def union(self, i, j):
        ip = self.find(i)
        jp = self.find(j)
        if self.rank[ip] > self.rank[jp]:
            self.parent[jp] = ip
        elif self.rank[ip] < self.rank[jp]:
            self.parent[ip] = jp
        else:
            self.rank[ip] += 1
            self.parent[jp] = ip

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

def solve0(seed_set, expansion_set):
    """
    merge set
    :param seed_set: set()
    :param expansion_set: list[]
    :return:
    """
    res = []
    for es in expansion_set:
        if seed_set.isdisjoint(es):
            continue
        else:
            newSet = set()
            res.append(newSet.union(es, seed_set))
    return res

def solve1(seed_set, expansion_set):
    """
    merge set from seed_set to expansion_set
    :param seed_set:
    :param expansion_set:
    :return:
    """
    res = [seed_set]
    level = [seed_set]
    while level:
        tmp = []
        for n in level:
            for es in expansion_set:
                if n.isdisjoint(es):
                    tmp.append(es)
                    res.append(es)
                    expansion_set.remove(es)
        level = tmp
    return merge(res)

def solve2(seed_set, expansion_set):
    return