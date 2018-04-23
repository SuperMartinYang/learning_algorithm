class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 1
        i = 0
        length = n - 1
        while length > 0:
            steps = i
            while steps < length:  # ->
                res[n - length - 1][steps] = cnt
                cnt += 1
                steps += 1
            steps = i
            while steps < length:  # |
                res[steps][length] = cnt  # v
                cnt += 1
                steps += 1
            steps = i
            while steps < length:  # <-
                res[length][n - steps - 1] = cnt
                cnt += 1
                steps += 1
            steps = i
            while steps < length:  # ^
                res[n - steps - 1][i] = cnt  # |
                cnt += 1
                steps += 1
            i += 1
            length = n - i - 1
        if cnt == n * n:
            res[n // 2][n // 2] = cnt
        return res

print(Solution().generateMatrix(5))