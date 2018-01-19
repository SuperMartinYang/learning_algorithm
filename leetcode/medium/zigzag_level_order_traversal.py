# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node_dict = {0: [root]}
        parent = [root]
        level = 1
        while parent:
            tmp = []
            for i in parent:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            node_dict[level] = tmp
            level += 1
            parent = tmp
        res = []
        for i, l in node_dict.items():
            tmp = []
            if i % 2 == 0:
                for j in l:
                    tmp.append(j.val)
            else:
                for j in l:
                    tmp.insert(0, j.val)
            res.append(tmp)

        return res

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(4)
root.right.left = TreeNode(20)
root.right.right = TreeNode(16)

s = Solution()
s.zigzagLevelOrder(root)