class SegmentTree:
    def __init__(self, low, high):
        self.root = TreeNode(low, high, 0)
    def addNode(self, parent, root, lo, hi, val):
        if not root:
            cur = TreeNode(parent.low, (parent.low + parent.high) // 2, 0)
        cur = root
        mid = (cur.low + cur.high) // 2
        if lo == cur.low and hi == cur.high:
            cur.val += val
        elif hi <= mid:
            self.addNode(root, root.left, lo, hi, val)
        elif lo >= mid:
            self.addNode(root, root.right, lo, hi, val)
        else:
            self.addNode(root, root.left, lo, mid, val)
            self.addNode(root, root.right, mid, hi, val)

class TreeNode:
    def __init__(self, low, high, val):
        self.low = low
        self.high = high
        self.val = val
        self.left = None
        self.right = None