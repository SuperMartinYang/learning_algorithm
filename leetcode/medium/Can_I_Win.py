class Solution(object):
    def can_i_win(self, maxChoosableInteger, desiredTotal):
        """
        given 0-maxChoosableInteger, and winning desiredTotal, check whether I can win
        :param maxChoosableInteger: int
        :param desiredTotal: int
        :return: bool
        """
        tgt = desiredTotal
        choices = list(range(1, maxChoosableInteger + 1))
        memo = {}
        if sum(choices) < tgt: return False

        def canWin(tot, chs):
            """

            :param tot: recent tot sum
            :param chs: remain choices
            :return: bool
            """
            key = (tot, str(chs))
            if key in memo: return memo[key]
            if chs and tot + chs[-1] >= tgt:
                memo[key] = True
                return True
            for i, ch in enumerate(chs):
                if not canWin(tot + ch, chs[:i] + chs[i + 1:]):
                    memo[key] = True
                    return True
            memo[key] = False
            return False

        res = canWin(0, choices)
        return res

print(Solution().can_i_win(10, 11))