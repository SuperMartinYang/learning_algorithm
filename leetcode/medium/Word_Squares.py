import copy
class Trie(object):
    def __init__(self):
        self.root = {}
    def add(self, word, i):
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['#'] = i    # used to find which word, '#' -> index for that word

    def isExist(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:
                return False
            else:
                cur = cur[ch]
        return '#' in cur

class Solution(object):
    def word_squares(self, words):
        # http://www.cnblogs.com/grandyang/p/6006000.html
        trie = Trie()
        for idx, w in enumerate(words):
            trie.add(w, idx)
        res = []
        tmp = []
        for w in words:
            tmp.append(w)
            self.helper(res, tmp, trie, 1, words)
        return res

    def helper(self, res, tmp, trie, level, words):
        if level == len(words):
            res.append(copy.deepcopy(tmp))
        # update tmp
        s = ''
        for i in range(level):
