class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        # dfs find the max for l, r, d, u
        m = len(image)
        n = len(image[0]) if m else 0
        d = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j, um, dm, lm, rm):
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != '1':
                return [um, dm, lm, rm]
            image[i][j] = '0'
            um = min(um, i)
            dm = max(dm, i)
            lm = min(lm, j)
            rm = max(rm, j)
            for p, q in d:
                tu, td, tl, tr = dfs(i + p, j + q, um, dm, lm, rm)
                um = min(um, tu)
                dm = max(dm, td)
                lm = min(lm, tl)
                rm = max(rm, tr)
            return [um, dm, lm, rm]
        um, dm, lm, rm = dfs(x, y, x, x, y, y)
        res = (dm - um + 1) * (rm - lm + 1)
        return res


print(Solution().minArea([['0','0','1','0'],['0','1','1','0'],['0','1','0','0']], 0, 2))