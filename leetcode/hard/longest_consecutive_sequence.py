class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        res = 0
        for n in nums:
            nums_set.add(n)

        for n in nums:
            down = n - 1
            while down in nums_set:
                nums_set.remove(down)
                down -= 1
            up = n + 1
            while up in nums_set:
                nums_set.remove(up)
                up += 1
            res = max(res, up - down - 1)
        return res
