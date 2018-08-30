class Solution(object):
    def valid_word_square(self, words):
        m = len(words)
        n = len(words[0]) if 0
        if m != n: return False
        for i in range(m):
            for j in range(n):
                if j >= m or i >= n or words[i][j] != words[j][i]:
                    return False
        return True