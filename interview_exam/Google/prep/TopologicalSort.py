import collections
def TopologicalSort(edges):
    """
    get the original sort
    :param edges: List of edges, directed, so can be sort
    :return:
    """
    graph = collections.defaultdict(list)
    inDegree = collections.defaultdict(int)
    nodes = set()
    for p, q in edges:
        graph[p].append(q)
        inDegree[q] += 1
        nodes.add(p)
        nodes.add(q)
    level = []
    res = []
    for n in nodes:
        if n not in inDegree:
            level.append(n)
    while level:
        tmp = []
        for n in level:
            res.append(n)
            for i in graph[i]:
                inDegree[i] -= 1
                if inDegree[i] == 0: tmp.append(i)
        level = tmp
    return res