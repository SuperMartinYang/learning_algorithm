# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t != None:
            return False
        if self.sameTree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, t1, t2):
        if t1 == None or t2 == None:
            if not t1 and not t2:
                return True
            return False
        if t1.val == t2.val:
            return self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right)
        return False
