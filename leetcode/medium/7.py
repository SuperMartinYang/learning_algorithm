# get the medium in two list
class Solution(object):
    def medium(self, list_A, list_B):
        """
        There are two sorted arrays nums1 and nums2 of size m and n respectively.
        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
        Example 1:
        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0

        Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5

        :param list_A:
        :param list_B:
        :return:
        """

        m,n = len(list_A),len(list_B)
        if m > n:
            list_A, list_B, m, n = list_B, list_A, n, m
        imin, imax, half_len = 0, m, int((m+n+1) / 2)        # use binary search to find a perfect i (position)
        while imin <= imax:
            i = int((imax + imin) / 2)
            j = half_len - i
            if i < m and list_A[i] < list_B[j - 1]:
                # case 1  A[i] too small, increase i, A[i] will be bigger, and B[j] will be smaller
                imin = i + 1
            elif i > 0 and list_B[j] < list_A[i - 1]:
                # case 2 A[i] too big
                imax = i - 1
            else:
                # case 3 i perfect          then get the median

                # deal with edge, when i == 0, A will not be divided, Since N > M, so left is all B, and parts of B and all A at right. vice verse
                if i == 0: max_of_left = list_B[j-1]
                elif j == 0: max_of_left = list_A[i-1]
                else: max_of_left = max(list_A[i-1],list_B[j-1])

                # when total items is odd, since N > M, so the bigger should be max_of_left
                if (m + n) % 2 == 1:
                    return max_of_left
                #like line 40
                if i == m: min_of_right = list_B[j]
                elif j == n: min_of_right = list_A[i]
                else: min_of_right = min(list_A[i], list_B[j])

                return (max_of_left + min_of_right) / 2.0


s = Solution()
print(s.medium(list_A=[1,2],list_B=[1,2]))