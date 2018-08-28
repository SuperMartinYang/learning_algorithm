# friend circle
import sys
# search



def bfs(relation, i, n, visited):
    level = [i]
    while level:
        tmp = []
        for i in level:
            visited[i] = True
            for j in range(n):
                if relation[i][j] and not visited[j]:
                    tmp.append(j)
        level = tmp

"""
10 
0
5 3 0
8 4 0
9 0 
9 0
3 0
0
7 9 0 
0 
9 7 0

"""

if __name__ == "__main__":
    # n
    n = int(sys.stdin.readline().strip())  # n people
    # relation table
    relation = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        # get line and init relation table
        line = sys.stdin.readline().strip()
        # int list
        values = [int(i) for i in line.split()]
        for v in values[:-1]:
            relation[i][v - 1] = 1  # True means, they know each other
            relation[v - 1][i] = 1
    # bfs find circle
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(relation, i, n, visited)
            visited[i] = True
            ans += 1
    print(ans)