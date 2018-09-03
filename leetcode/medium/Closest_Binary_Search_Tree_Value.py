class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution(object):
    def closest_binary_search_tree_value(self, root, target):
        """
        :param root: TreeNode
        :param target: int
        :return: TreeNode
        """
        if not root: return None
        nxt = root.right if root.val > target else root.left
        res = self.closest_binary_search_tree_value(nxt, target)
        return res if abs(res - target) < abs(root.val - target) else root.val