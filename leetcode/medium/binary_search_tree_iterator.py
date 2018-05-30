# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root:
            self.root = root
            self.head = root
            self.formLinksThruInorder(self.head)
            while self.root.left:
                self.root = self.root.left  # smallest
        else:
            self.root = None
            self.head = None

    def formLinksThruInorder(self, head):
        if not head:
            return
        if head.left:
            predecessor = self.largestOnLeft(head)
            if predecessor.right:
                return
            predecessor.right = head
        else:
            predecessor = self.noLeftNodePredecessor(head)
            if predecessor:
                predecessor.right = head
        self.formLinksThruInorder(head.left)
        self.formLinksThruInorder(head.right)

    def largestOnLeft(self, head):
        left = head.left
        while left.right:
            left = left.right
        return left

    def noLeftNodePredecessor(self, head):
        it = self.head
        predecessor = None
        while it.val != head.val:
            if head.val < it.val:
                it = it.left
            else:
                predecessor = it
                it = it.right
        return predecessor

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root != None

    def next(self):
        """
        :rtype: int
        """
        nextVal = self.root.val
        self.root = self.root.right
        return nextVal


class Solution2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push(root)

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.push(node.right)
        return node.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())