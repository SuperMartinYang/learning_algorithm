def BFS(node):
    visited = []    # when there's cyclic, acyclic don't need visited
    level = [node] if node else []
    while level:
        tmp = []
        for n in level:
            # do some stuff here
            # when some condition meet
            if visited[n]: continue
            tmp.append()
            visited[n] = True
        level = tmp
    return