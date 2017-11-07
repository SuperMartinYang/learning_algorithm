class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        elif numRows == 1:
            result = self.generate(0)
            result.append([1])
        # elif numRows == 2:
        #     result = self.generate(1)
        #     return result.append([1, 1])
        else:
            result = self.generate(numRows - 1)
            pre = result[numRows - 2]
            pre_len = len(pre)
            nx = []
            nx.append(pre[0])
            for i in range(1,pre_len):
                nx.append(pre[i-1] + pre[i])
            nx.append(pre[len(pre) - 1])
            result.append(nx)
        return result


s = Solution()

print(s.generate(5))