class Solution(object):
    def swap_distance1(self, str1, str2):
        # swap once, whether can make two str equal
        if len(str1) != len(str2): return False
        i = 0
        id1, id2 = None, None
        while i < len(str1):
            if str1[i] != str2[i]:
                if id1 is None:
                    id1 = i
                elif id2 is None:
                    id2 = i
                else: return False
            i += 1
        if str1[id1] == str2[id2] and str1[id2] == str2[id1]:
            return True
        return False

    def swap_distance2(self, str1, str2):
        """
        can str1 become str2 by swap multiple times
        :param str1: string
        :param str2: string
        :return: bool
        """


    def swap_distance3(self, str1, str2):
        """
        minimum swap steps to make str1 equals str2
        :param str1:
        :param str2:
        :return:
        """

print(Solution().swap_distance1('abc', 'cba'))