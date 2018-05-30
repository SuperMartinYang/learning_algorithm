# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        brute force recursive, TLE
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes2(self, root):
        """
        brute force iteration, TLE
        :param root:
        :return:
        """
        if not root:
            return 0
        q = [root]
        cnt = 1
        while q:
            tmp = q.pop()
            if tmp.left:
                q.append(tmp.left)
                cnt += 1
            if tmp.right:
                q.append(tmp.right)
                cnt += 1

        return cnt

    def countNode3(self, root):
        """
        cuz it's complete, compute using height, T(n) = log(n)
        :param root:
        :return:
        """
        def height(node):
            return -1 if not node else 1 + height(node.left)

        h = height(root)
        return 0 if h == -1 else (1 << h) + self.countNode3(root.right) if height(root.right) == h - 1 else 1 << (
                    h - 1) + self.countNode3(root.left)
