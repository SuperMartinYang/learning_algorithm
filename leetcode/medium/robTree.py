# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stoleRoot = root.val + self.rob(root.right.left if root.right else None) + self.rob(root.right.right if root.right else None) + self.rob(root.left.left if root.left else None) + self.rob(root.left.right if root.left else None)
        dontRoot = self.rob(root.right) + self.rob(root.left)
        return max(stoleRoot, dontRoot)

    def rob2(self, root):
        # res[0] rob root, res[1] not rob root
        res = self.robSub(root)
        return max(res[0], res[1])

    def robSub(self, root):
        if not root:
            return 0
        left = self.robSub(root.left)
        right = self.robSub(root.right)

        return [root.val + left[0] + right[0], left[1] + right[1]]