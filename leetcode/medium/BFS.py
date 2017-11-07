def bfs(s, adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[u] = i
                    parent[v] = u
                    nxt.append(v)
        frontier = nxt
        i += 1

