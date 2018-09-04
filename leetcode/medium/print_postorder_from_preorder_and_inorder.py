class Solution(object):
    def print_postorder_from_preorder_and_inorder(self, preorder, inorder):
        postorder = []
        if not preorder: return preorder
        idx = inorder.index(preorder[0])
        left = self.print_postorder_from_preorder_and_inorder(preorder[1:1 + idx], inorder[:idx])
        right = self.print_postorder_from_preorder_and_inorder(preorder[1 + idx:], inorder[idx + 1:])
        postorder.extend(left)
        postorder.extend(right)
        postorder.append(preorder[0])
        return postorder


print(Solution().print_postorder_from_preorder_and_inorder([1,2,3,4,5], [3,2,4,1,5]))