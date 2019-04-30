import unittest
class Solution:

    def maximum_product(self, nums, k):
        """
        params: nums: list
        params: k: int
        """
        if len(nums) < k: return 0
        nums.sort()
        res = 1
        if nums[0] * nums[-1] >= 0:
            for i in range(k):
                res *= nums[len(nums) - 1 - i]
            return res
        r = len(nums) - 1
        l = 0
        while k > 0:
            if (k & 1) == 1:
                res *= nums[r]; r -= 1
            else:
                if nums[r] * nums[ r - 1] > nums[l] * nums[l + 1]:
                    res *= nums[r] * nums[r - 1]; r -= 2
                else:
                    res *= nums[l] * nums[l + 1]; l += 2 
                k -= 1
            k -= 1
        return res

class Tests(unittest.TestCase):
    def test_max_pro(self):
        self.assertEqual(Solution().maximum_product([3,2,1,4,5,7], 3), 140)

    def test_max(self):
        self.assertEqual(Solution().maximum_product([3,2,1,3,5,7], 2), 140)
    
if __name__ == "__main__":
    unittest.main()
    # print(Solution().maximum_product([3,2,1,4,5,7], 3))
    print('Hello, finished')