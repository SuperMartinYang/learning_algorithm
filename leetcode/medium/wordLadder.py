import collections
import string

class Solution(object):
    def ladderLength1(self, beginWord, endWord, wordList):
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
        
    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # wrong
        wordList= set(wordList)
        if endWord not in wordList: return 0
        # bfs
        # level = [[beginWord, 0]] if len(beginWord) == len(endWord) else []
        
        # dfs can use hashmap, will be faster
        mp = collections.defaultdict(int)
        mp[endWord] = 0
        def dfs(curWord):
            if curWord in mp: return mp[curWord]
            res = 1e9
            for i in range(len(curWord)):
                for ch in string.ascii_lowercase:
                    newWord = curWord[:i] + ch + curWord[i + 1:]
                    if newWord not in wordList: continue
                    st = dfs(newWord)
                    if st != 1e9: 
                        res = min(res, st + 1)
            mp[curWord] = res
            return res
        
        return dfs(beginWord)
    
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        left = {beginWord}
        right = {endWord}
        visited = set()
        cnt = 0
        while (left and right):
            if len(left) > len(right):
                left, right = right, left
            nxt = set()
            cnt += 1
            for s in left:
                for i in range(len(s)):
                    for ch in string.ascii_lowercase:
                        newS = s[:i] + ch + s[i + 1:]
                        if newS in right: return cnt + 1
                        if newS in wordSet and newS not in visited:
                            nxt.add(newS)
                            visited.add(newS)
            left = nxt
        return 0

s = Solution()
print(s.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))