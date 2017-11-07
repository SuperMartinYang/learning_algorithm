# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or nums == []:
            return 0;
        numslen = len(nums)
        root = TreeNode(nums[numslen/2])
        root.left = self.sortedArrayToBST(nums[0: numslen/2])
        root.right = self.sortedArrayToBST(nums[numslen/2 + 1: numslen])

        return root