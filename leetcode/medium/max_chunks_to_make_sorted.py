class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = 0
        start = 0
        i = 1
        while start < len(arr) and i <= len(arr):
            if max(arr[start:i]) == i - 1:
                cnt += 1
                start = i
                i += 1
            else:
                i += 1
        return cnt

s = Solution()
print s.maxChunksToSorted([4,3,2,1,0])