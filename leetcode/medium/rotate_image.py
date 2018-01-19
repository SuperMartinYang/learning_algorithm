class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        def rotate_single(i, j):
            tmp = matrix[j][i]
            matrix[j][i] = matrix[n - 1 - i][j]

            tmp2 = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = tmp

            tmp = matrix[n - 1 - j][n - 1 - i]
            matrix[n - 1 - j][n - 1 - i] = tmp2

            matrix[n - 1 - i][j] = tmp

        n = len(matrix)
        for j in range(n // 2):
            for i in range(j, n - j - 1):
                rotate_single(i, j)
        return matrix

# [[2,29,20,26,16,28],
#  [12,27,9,25,13,21],
#  [32,33,32,2,28,14],              ###################
#  [13,14,32,27,22,26],             ##  Original
#  [33,1,20,7,21,7],                ##################
#  [4,24,1,6,32,34]]
#
# [[4,33,13,32,12,2],
#  [24,1,7,33,27,29],
#  [1,20,32,2,14,20],               ###################
#  [6,28,32,27,25,26],              ##  Wrong
#  [32,21,22,9,13,16],              ################
#  [34,7,26,14,21,28]]
#
# [[4,33,13,32,12,2],
#  [24,1,14,33,27,29],
#  [1,20,32,32,9,20],               #################
#  [6,7,27,2,25,26],                ##  Right
#  [32,21,22,28,13,16],             #################
#  [34,7,26,14,21,28]]


s = Solution()
print(s.rotate([[2,29,20,26,16,28],
 [12,27,9,25,13,21],
 [32,33,32,2,28,14],
 [13,14,32,27,22,26],
 [33,1,20,7,21,7],
 [4,24,1,6,32,34]]))