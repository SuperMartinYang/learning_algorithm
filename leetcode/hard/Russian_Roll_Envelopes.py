class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        size = 0
        for e in envelopes:
            # binary search to update dp
            lo, hi = 0, size
            while lo < hi:
                mid = (hi + lo) / 2
                if dp[mid] < e[1]:
                    lo = mid + 1
                else:
                    hi = mid
            dp[lo] = e[1]
            size = max(lo + 1, size)
        return size