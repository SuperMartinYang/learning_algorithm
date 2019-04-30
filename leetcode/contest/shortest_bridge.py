class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # bidirection bfs
        m = len(A)
        n = len(A[0]) if m else 0
        root = list(range(m * n + 1))
        root[-1] = -1
        d = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def find(idx):
            if idx != root[idx]:
                root[idx] = find(root[idx])
            return root[idx]

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    for p, q in d:
                        x, y = i + p, j + q
                        if 0 <= x < m and 0 <= y < n:
                            if A[x][y] == 1:
                                ri, rx = find(i * n + j), find(x * n + y)
                                if ri != rx: root[ri] = rx
                            else:
                                root[x * n + y] = -1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    start = (i, j)
                    break
        print(root)
        one = find(start[0] * n + start[1])
        level = [(start[0], start[1], 1)]
        visited = set()
        visited.add(start)
        while level:
            tmp = []
            for nd in level:
                i, j, lv = nd
                for p, q in d:
                    x, y = i + p, j + q
                    if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited: continue
                    rx = find(x * n + y)
                    if rx != -1 and rx != one:
                        return lv - 1
                    if rx == one: lv = 1
                    visited.add((x, y))
                    tmp.append((x, y, lv + 1))
            level = tmp
        return -1

A = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print(Solution().shortestBridge(A))
