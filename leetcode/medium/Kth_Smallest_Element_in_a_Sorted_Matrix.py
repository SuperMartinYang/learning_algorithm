# import heapq
import itertools
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        hp = []
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        for i in range(col):
            heapq.heappush(hp, (matrix[0][i], 0, i))
        for i in range(k - 1):
            tmp = heapq.heappop(hp)
            if tmp[1] == row - 1:
                continue
            heapq.heappush(hp, (matrix[tmp[1] + 1][tmp[2]], tmp[1] + 1, tmp[2]))
        return heapq.heappop(hp)[0]