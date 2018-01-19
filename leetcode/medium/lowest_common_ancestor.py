class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root is p or root is q:
            return root
        mayleft = self.lowestCommonAncestor(root.left, p, q)
        mayright = self.lowestCommonAncestor(root.right, p, q)

        if mayleft is not None and mayright is not None:
            return root
        else:
            return mayright or mayleft
