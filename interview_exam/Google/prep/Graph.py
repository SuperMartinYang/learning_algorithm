import collections
def Graph(glist):
    # form graph
    # use dic
    graph = collections.defaultdict(list)
    for idx, ilist in enumerate(glist):
        for i in ilist:
            graph[idx].append(i)
    return graph