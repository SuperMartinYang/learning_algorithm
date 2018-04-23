# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, tsum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(node, rem, pl):
            if rem == 0 and not node.left and not node.right:
                res.append([i for i in pl])
            if node.left and rem - node.left.val >= 0:
                pl.append(node.left.val)
                helper(node.left, rem - node.left.val, pl)
                pl.pop()
            if node.right and rem - node.right.val >= 0:
                pl.append(node.right.val)
                helper(node.right, rem - node.right.val, pl)
                pl.pop()
            return

        helper(root, tsum - root.val, [root.val])
        return res

root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(8)
root.left = left
root.right = right
n11 = TreeNode(11)
left.left = n11
n11.right = TreeNode(2)
n11.left = TreeNode(7)
right.left = TreeNode(13)
n4 = TreeNode(4)
right.right = n4
n4.right = TreeNode(1)
n4.left = TreeNode(5)

s = Solution()
print(s.pathSum(root, 22))