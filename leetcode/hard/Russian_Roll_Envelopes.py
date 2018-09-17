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
                mid = (hi + lo) // 2
                if dp[mid] < e[1]:
                    lo = mid + 1
                else:
                    hi = mid
            print(dp[lo], e[1])
            dp[lo] = e[1]
            size = max(lo + 1, size)
        return size

print(Solution().maxEnvelopes([[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]))