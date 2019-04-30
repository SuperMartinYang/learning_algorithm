import unittest
class Solution:
    def arr2range(self, arr):
        res = []
        if not arr: return res
        start, end = arr[0], arr[0]
        for val in arr[1:]:
            if val == end + 1: end += 1
            else:
                res.append([start, end])
                start, end = val, val
        res.append([start, end])
        return res

class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().arr2range([1,2,3,4,6,7,10]), [[1,4], [6,7], [10, 10]])


if __name__ == "__main__":
    unittest.main()