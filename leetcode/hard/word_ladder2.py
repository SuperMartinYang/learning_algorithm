import string
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        def helper(newS, path, maskL):
            if newS == endWord:
                res[len(path)].append([i for i in path])
            idx = 0
            while idx < len(endWord):
                if maskL[idx] == 'o':
                    idx += 1
                    continue
                for i in string.ascii_lowercase:
                    tmpS = newS[:idx] + i + newS[idx + 1:]
                    if tmpS in wordList:
                        path.append(tmpS)
                        maskL[idx] = 'o'
                        helper(tmpS, path, maskL)
                        maskL[idx] = '*'
                        path.pop()
                idx += 1
            return

        helper(beginWord, [beginWord], ['*'] * len(endWord))
        minLen = min(res.keys())
        return res[minLen]


s = Solution()
print(s.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
