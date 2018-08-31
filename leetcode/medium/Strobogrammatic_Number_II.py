class Solution(object):
    def strobogrammatic_number_ii(self, n):
        """
        get the count of all strobogrammatic number which length is n
        1: 0 1 8
        2: 11 69 88 96
        3: 101 609 808 906 111 619 818 916 181 689 888 986
        :param n:
        :return:
        """
        if n == 1: return 3
        if n == 2: return 4
        return 4 * self.strobogrammatic_number_ii(n - 2)

    def strobogrammatic_number_ii_(self, n):
        """
        find all strobogrammatic number which length is n
        :param n:
        :return: list
        """
        if n == 1: return ['0', '1', '8']
        if n == 2: return ['11', '88', '69', '96']
        pre = self.strobogrammatic_number_ii_(n - 2)
        res = []
        for a in pre:
            res.append('1' + a + '1')
            res.append('8' + a + '8')
            res.append('6' + a + '9')
            res.append('9' + a + '6')

        return res

print(Solution().strobogrammatic_number_ii_(4))