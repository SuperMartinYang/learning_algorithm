class Solution(object):
    def medium_of_two_sorted_array(self, nums1, nums2):
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2
        return (self.findKth(nums1, nums2, k1) + self.findKth(nums1, nums2, k2)) / 2

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2): return self.findKth(nums2, nums1, k)
        m, n = len(nums1), len(nums2)
        if m == 0: return nums2[k - 1]
        if k == 1: return min(nums1[0], nums2[0])
        i, j = min(m, k // 2), min(n, k // 2)
        if nums1[i - 1] > nums2[j - 1]:
            return self.findKth(nums1, nums2[j:], k - j)
        else:
            return self.findKth(nums1[i:], nums2, k - i)

print(Solution().medium_of_two_sorted_array([1,3,5,7], [2,3,5]))
print(Solution().medium_of_two_sorted_array([1], []))
