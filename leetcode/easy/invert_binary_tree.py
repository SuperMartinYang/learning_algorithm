# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or (not root.left and not root.right):
            return root
        new_root = TreeNode(root.val)
        if not root.right and root.left:
            new_root.right = self.invertTree(root.left)
        elif not root.left and root.right:
            new_root.left = self.invertTree(root.right)
        else:
            new_root.left = self.invertTree(root.right)
            new_root.right = self.invertTree(root.left)

        return new_root