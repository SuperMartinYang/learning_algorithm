class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        len_word = len(beginWord)
        finMin = float('inf')
        for i in range(len_word):
            for j in range(1, 27):
                tmp = beginWord[:i] + chr(0x60 + j) + beginWord[i + 1:]
                for k in range(len(wordList)):
                    if wordList[k] == tmp:
                        t = self.ladderLength(tmp, endWord, wordList[:k] + wordList[k + 1:])
                        if t:
                            tmpMin = 1 + t
                            if tmpMin < finMin:
                                finMin = tmpMin
        if finMin != float('inf'):
            return finMin
        return 0

s = Solution()
print s.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])