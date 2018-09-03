class Solution(object):
    def nim_game(self, n):
        """
        can I win
        :param n: int, stone on the table
        :return: bool
        """
        return n % 4 != 0