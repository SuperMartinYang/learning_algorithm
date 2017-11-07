class Solution(object):
    def path_sum(self, root, sum_):
        '''

        You are given a binary tree in which each node contains an integer value.
        Find the number of paths that sum to a given value.
        The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
        The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
        Example:
        root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

              10
             /  \
            5   -3
           / \    \
          3   2   11
         / \   \
        3  -2   1

        Return 3. The paths that sum to 8 are:

        1.  5 -> 3
        2.  5 -> 2 -> 1
        3. -3 -> 11
        :param root: TreeNode
        :param sum: int
        :return: int
        '''
        if root == None:
            return 0
        sumleft = sumright = sumroot = 0
        sumroot += self.rootSum(root, sum_)
        sumleft += self.pathSum(root.left, sum_)
        sumright += self.pathSum(root.right, sum_)

        return sumleft + sumroot + sumright

    def rootSum(self, root, sum_):
        sum1 = 0
        if root == None:
            return 0
        if sum_ - root.val == 0:
            sum1 += 1
        left = self.rootSum(root.left, sum_ - root.val)
        right = self.rootSum(root.right, sum_ - root.val)

        return left + right + sum1