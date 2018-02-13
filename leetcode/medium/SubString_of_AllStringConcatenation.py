class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def initDict():
            wordDict = {}
            for word in words:
                if word in wordDict.keys():
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
            return wordDict

        wordLen = len(words[0]) if len(words) != 0 else 0
        wordsLen = wordLen * len(words)
        wordD = initDict()
        res = []
        for i in range(len(s) - wordsLen + 1):
            if self.isConcat(wordD, s, i, wordLen, wordsLen):
                res.append(i)
            wordD = initDict()
        return res

    def isConcat(self, wordDict, s, start, wordLen, wordsLen):
        for i in range(start, start + wordsLen, wordLen):
            if not wordDict.get(s[i:i + wordLen]):
                return False
            if wordDict[s[i:i + wordLen]] > 0:
                wordDict[s[i:i + wordLen]] -= 1
            else:
                return False
        return True


print(Solution().findSubstring("wordgoodgoodgoodbestword",
["word","good","best","good"]))