class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary.sort()
        def find(root):
            lo, hi = 0, len(dictionary) - 1
            while lo + 1 < hi:
                mid = (hi - lo) // 2 + lo
                if root > dictionary[mid]:
                    lo = mid
                elif root < dictionary[mid]:
                    hi = mid
                else:
                    return mid
            if dictionary[lo] == root: return lo
            if dictionary[hi] == root: return hi
            return -1

        def tryReplace(index):
            for i in range(1, len(sentence[index])):
                dictIdx = find(sentence[index][:i])
                if dictIdx != -1:
                    return dictionary[dictIdx]
            return sentence[index]

        sentence = sentence.split()
        for i in range(len(sentence)):
            sentence[i] = tryReplace(i)
        return ' '.join(sentence)

    def replaceWords2(self, dictionary, sentence):
        """
        Use trie tree
        :param dictionary:
        :param sentence:
        :return:
        """


print(Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))