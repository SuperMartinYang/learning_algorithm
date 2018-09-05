class Solution(object):
    def __init__(self):
        self.dic = set()

    def buildDict(self, words):
        for w in words:
            self.dic.add(w)

    def search(self, word):
        for w in self.dic:
            if word == w or len(word) != len(w): continue
            i = 0
            cnt = 0
            while i < len(w):
                if word[i] != w and cnt < 1:
                   cnt += 1
                i += 1
            if cnt == 1: return True
        return False

s = Solution()
s.buildDict(['hello', 'leetcode'])
print(s.search('hhllo'))
print(s.search('hello'))
print(s.search('leetcodee'))

