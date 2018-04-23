import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        bidirectional BFS
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        length = 1
        strLen = len(beginWord)
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                tl = beginSet
                beginSet = endSet
                endSet = tl
            for word in beginSet:
                tmpSet = set()
                for i in range(strLen):
                    for c in string.ascii_lowercase:
                        tw = word[:i] + c + word[i + 1:]
                        if tw in endSet:
                            return length + 1
                        if tw not in visited and tw in wordList:
                            tmpSet.add(tw)
                            visited.add(tw)
            length += 1
            beginSet = tmpSet
        return 0



