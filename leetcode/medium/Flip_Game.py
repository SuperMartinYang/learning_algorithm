class Solution(object):
    def flip_game(self, gameS):
        res = []
        for i in range(1, len(gameS)):
            if gameS[i] == '+' and gameS[i - 1] == '+':
                res.append(gameS[:i - 1] + '--' + gameS[i + 1:])
        return res