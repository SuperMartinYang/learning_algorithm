class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        nearly the same as Kth_Smallest_Element_in_a_Sorted_Matrix
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        m, n = len(nums1), len(nums2)
        if k >= m * n:
            return [[nums1[i], nums2[j]] for i in range(len(nums1)) for j in range(len(nums2))]

        hp = []
        res = []
        for i in range(n):
            heapq.heappush(hp, (nums1[0] + nums2[i], 0, i))
        for i in range(k):
            tmp = heapq.heappop(hp)
            res.append([nums1[tmp[1]], nums2[tmp[2]]])
            if tmp[1] == m - 1:
                continue
            heapq.heappush(hp, (nums1[tmp[1] + 1] + nums2[tmp[2]], tmp[1] + 1, tmp[2]))

        return res