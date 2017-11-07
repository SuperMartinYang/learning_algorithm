# To-do

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        Given two binary trees, write a function to check if they are equal or not.
        Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q == None:
            return True
        elif (not q and p) or (q and not p) or (q.val != p.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
