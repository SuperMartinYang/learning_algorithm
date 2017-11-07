class BSTNode(object):
    """
    A node in the vanilla BST tree.
    """
    def __init__(self, parent, k):
        """
        Creates a node.
        :param parent: node's parent
        :param k: node's key
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """
        Find and return the node with key k from the subtree
        rooted at this
        :param k: nodes with key k
        :return: node
        """
        if self.key == k:
            return self
        if k > self.key:
            if self.right is None:
                return None
            else:
                return self.right.find(k)
        else:
            if self.left is None:
                return None
            else:
                return self.left.find(k)

    def find_min(self):
        """
        Find the node with the minimum key in the subtree rooted at this node.
        :return:
        """
        cur_node = self
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node

    def next_larger(self):
        """
        Find the node with the next larger key (the successor) in the BST
        :return:
        """
        if self.right is not None:
            return self.right.find_min()
        cur_node = self
        while cur_node.parent is not None and cur_node.parent.right is cur_node:
            cur_node = cur_node.parent
        return cur_node.parent

    def insert(self, node):
        """
        insert a node into the subtree rooted at this node
        :param k:
        :return:
        """
        if node is None:
            return
        if node.key > self.key:
            if self.right is None:
                self.right = node
            else:
                self.insert(self.right)
        elif node.key < self.key:
            if self.left is None:
                self.left = node
            else:
                self.insert(self.left)

    def delete(self):
        """
        delete and return this node from the BST.
        :return:
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.left
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            s.key, self.key = self.key, s.key
            return s.delete()


class BST(object):
    def __init__(self):
        self.root = None

    def find(self, k):
        return self.root and self.root.find(k)

    def find_min(self):
        """
        return the minimum node of the BST
        :return:
        """
        return self.root and self.root.find_min()

    def insert(self, k):
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def delete(self, k):
        """
        delete and return a node with key k if it exists from the BST
        :param k:
        :return:
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            # since in BSTNode class, delete assume that node has parent
            pseudoroot = BSTNode(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        """
        return the node that contains the next larger (the successor) key in
        the BST in relation to the node with key k
        :return:
        """
        node = self.find(k)
        return node and node.next_larger()


# the variation of BST Tree
class MinBSTNode(BSTNode):
    """
    A node in BST which is augmented to keep track of the node with the
    minimum key in the subtree rooted by this node
    :param BSTNode:
    :return:
    """
    def __init__(self, parent, key):
        super(MinBSTNode, self).__init__(parent, key)
        self.min = self

