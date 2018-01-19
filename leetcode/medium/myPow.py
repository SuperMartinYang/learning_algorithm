class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        btou = [None for _ in range(abs(n) + 1)]
        btou[0] = 1
        btou[1] = x
        def my(x, n):
            mid = abs(n) // 2
            if btou[mid] and btou[abs(n) - mid]:
                btou[abs(n)] = btou[mid] * btou[abs(n) - mid]
                res = btou[abs(n)]
            else:
                res = my(x, abs(n) - mid) * my(x, mid)
            if n < 0:
                return 1 / res
            return res
        return my(x, n)

s = Solution()
print s.myPow(-2.000, 0)