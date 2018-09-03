class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution(object):
    def closest_binary_search_tree_value_ii(self, root, target, k):
        """
        :param root:
        :param target:
        :param k:
        :return:
        """
        # use priority queue
        hq = []

        def traverse(node):
            if not node: return
            if len(hq) > k:
                heapq.heappop(hq)
            heapq.heappush([-abs(node.val - target), node.val])
            traverse(node.left)
            traverse(node.right)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(hp)[1])
        return res