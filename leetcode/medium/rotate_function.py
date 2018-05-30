class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        tot_sum = sum(A)
        F = [0 for _ in range(len(A))]
        f = 0
        for i in range(len(A)):
            f += i * A[i]
        F[0] = f
        for i in range(1, len(A)):
            F[i] = F[i - 1] + tot_sum - len(A) * A[len(A) - i]

        return max(F)


print(Solution().maxRotateFunction([i for i in range(1, 11)]))