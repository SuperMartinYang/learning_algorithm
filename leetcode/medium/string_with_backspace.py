class Solution(object):
    def string_with_backspace(self, str1, str2):
        """
        check whether these 2 string is the same
        :param str1:
        :param str2:
        :return:
        """
        def simplify(s):
            stack = []
            for ch in s:
                if ch == '<' and stack:
                    stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)
        return simplify(str1) == simplify(str2)

    def string_with_backspace_no_stack(self, str1, str2):
        """
        two point to solve this problem
        :param str1:
        :param str2:
        :return:
        """
        s1, e1, s2, e2 = 0, 0, 0, 0
        while e1 < len(str1) or e2 < len(str2):
            while 0 <= e1 < len(str1) and str1[e1] == '<':
                s1 = s1 - 1 if s1 > 0 else 0
                e1 += 1
            while 0 <= e2 < len(str2) and str2[e2] == '<':
                s2 = s2 - 1 if s2 > 0 else 0
                e1 += 1
            if str1[s1] != str2[s2]:
                return False
            s1 += e1
            s2 += e2
        return True