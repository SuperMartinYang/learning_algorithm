def dfs_visit(s,Adj, parent):
    for i in Adj[s]:
        if i not in parent:
            parent[i] = s
            dfs_visit(i, Adj)

def dfs(v,Adj):
    parent = {}
    for i in v:
        if i not in parent:
            parent[i] = None
            dfs_visit(i, Adj, parent)

