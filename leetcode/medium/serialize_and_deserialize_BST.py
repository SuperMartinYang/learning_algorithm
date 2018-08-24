# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = [root.val]
        level = [root]
        while level:
            tmp_level = []
            for node in level:
                if node.left:
                    tmp_level.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append(None)
                if node.right:
                    tmp_level.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append(None)
            level = tmp_level
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data.split(',')
        data[0] = data[0][1:]
        data[-1] = data[-1][:-1]
        for i in range(len(data)):
            data[i] = int(data[i]) if data[i].strip() != 'None' else None
        root = TreeNode(data[0])
        level = [root]
        i = 1
        while level and i < len(data):
            tmp_level = []
            for node in level:
                if data[i] is not None:
                    node.left = TreeNode(data[i])
                    tmp_level.append(node.left)
                if data[i + 1] is not None:
                    node.right = TreeNode(data[i + 1])
                    tmp_level.append(node.right)
                i += 2
            level = tmp_level
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))