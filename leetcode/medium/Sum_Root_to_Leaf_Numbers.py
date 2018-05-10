# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        stack
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodeStack = [root]
        mySum = 0
        while nodeStack:
            node = nodeStack.pop()
            if not node.left and not node.right:
                mySum += node.val
            if node.left:
                node.left.val = node.val * 10 + node.left.val
                nodeStack.append(node.left)
            if node.right:
                node.right.val = node.val * 10 + node.right.val
                nodeStack.append(node.right)
        return mySum

    def sumNumbers2(self, root):
        def solver(root, ssum):
            if not root:
                return 0
            if not root.left and not root.right:
                return ssum * 10 + root.val
            return solver(root.left, ssum * 10 + root.val) + solver(root.right, ssum * 10 + root.val)

        return solver(root, 0)
