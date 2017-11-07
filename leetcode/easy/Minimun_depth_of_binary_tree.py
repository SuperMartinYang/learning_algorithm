# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        left_depth = self.minDepth(root.left)
        if left_depth == 0:
            left_depth = 10000
        right_depth = self.minDepth(root.right)
        if right_depth == 0:
            right_depth = 10000

        return min(right_depth, left_depth) + 1
