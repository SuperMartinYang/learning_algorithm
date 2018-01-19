class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # combine all possible choice, find the min, add to the result
        idx = [0 for _ in range(len(primes))]  # if use idx[x] product a duplicate one, skip, which means move to the lightly bigger one.
        ugly = [0 for _ in range(n)]
        val = [1 for _ in range(len(primes))]
        nxt = 1
        for i in range(n):
            ugly[i] = nxt
            nxt = float('inf')

            for j in range(len(primes)):
                if val[j] == ugly[i]:
                    val[j] = ugly[idx[j]] * primes[j]
                    idx[j] += 1
                nxt = min(nxt, val[j])
        return ugly[n - 1]

    def nthSuperUglyNumber2(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # combine all possible choice, find the min, add to the result
        idx = [0 for _ in range(len(primes))]
        ugly = [0 for _ in range(n)]
        ugly[0] = 1
        for i in range(1, n):
            ugly[i] = float('inf')

            for j in range(len(primes)):
                ugly[i] = min(ugly[i], ugly[idx[j]] * primes[j])

            for j in range(len(primes)):
                if ugly[idx[j]] * primes[j] == ugly[i]:
                    idx[j] += 1
        return ugly[n - 1]


s = Solution()
print s.nthSuperUglyNumber2(12, [2, 7, 13, 19])
