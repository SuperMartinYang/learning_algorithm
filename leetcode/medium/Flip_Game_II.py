class Solution(object):
    def flip_game_ii(self, gameS):
        """
        canWin
        :param gameS:
        :return: bool
        """
        for i in range(1, len(gameS)):
            if gameS[i] == '+' and gameS[i - 1] == '+':
                if not self.flip_game_ii(gameS[:i - 1] + '--' + gameS[i + 1:]):
                    return True
        return False
