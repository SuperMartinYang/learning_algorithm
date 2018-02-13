class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        orderStack = []
        for i in range(len(preorder) - 1, -1, -1):
            if preorder[i] == '#':
                orderStack.append('#')
            else:
                if len(orderStack) < 2:
                    return False
                else:
                    orderStack.pop()
        return True if len(orderStack) == 1 else False

s = Solution()
print s.isValidSerialization([9,3,4,'#','#',1,'#','#',2,'#','6','#','#'])