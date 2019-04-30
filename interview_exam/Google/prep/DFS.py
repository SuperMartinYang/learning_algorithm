def DFS():
    visited = []
    def dfs(i):
        # check condition and whether visited
        # go to the next step
        visited[i] = True
        dfs()

    # when some condition meet
    dfs(0)
    return