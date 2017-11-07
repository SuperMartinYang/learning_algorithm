# To-do

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root_list = []
        len = 0
        if root == None:
            return True
        if root.left and root.right:
            if root.left.val == root.right.val:
                root_list.append(root.left)
                root_list.append(root.right)
                len += 2
            else:
                return False
        else:
            return False

        while len > 0:
            rt = root_list.pop()
            lt = root_list.pop()
            if not rt.right and not lt.left and not rt.left and not lt.right:
                len -= 2
            elif rt.right and rt.left and lt.right and lt.left:
                if rt.right == lt.left and rt.left == lt.right:
                    root_list.append(rt.right)
                    root_list.append(lt.left)
                    root_list.append(rt.left)
                    root_list.append(lt.right)
                    len += 2
                else:
                    return False
            elif not rt.right and not lt.left and rt.left and lt.right:
                if rt.left == lt.right:
                    root_list.append(lt.right)
                    root_list.append(rt.left)
                else:
                    return False
            elif rt.right and lt.left and not rt.left and not lt.right:
                if rt.right == lt.left:
                    root_list.append(lt.left)
                    root_list.append(rt.right)
                else:
                    return False
            else:
                return False
        return True

