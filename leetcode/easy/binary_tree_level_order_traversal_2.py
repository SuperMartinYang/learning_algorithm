# To-do

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        root_list = []
        root_list.append(root)
        while len(root_list) != 0:
            root = root_list.pop()
            if root.right != None:
                root_list.append(root.right)
            if root.left != None:
                root_list.append(root.left)
