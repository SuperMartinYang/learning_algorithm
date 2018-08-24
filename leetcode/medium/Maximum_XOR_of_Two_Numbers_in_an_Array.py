class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # form trie
        root = {}
        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                tmp = (num & (1 << i)) >> i
                if tmp not in cur:
                    cur[tmp] = {}
                cur = cur[tmp]
        # go through trie
        res = 0
        for num in nums:
            cur = root
            tmp_max = 0
            for i in range(31, -1, -1):
                tmp = (num & (1 << i)) >> i
                if 0 in cur and 1 in cur:
                    if tmp == 1:
                        var = 0
                    else:
                        var = 1
                else:
                    var = 0 if 0 in cur else 1
                cur = cur[var]
                tmp_max += (tmp << i) ^ (var << i)
            res = max(res, tmp_max)
        return res


print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))