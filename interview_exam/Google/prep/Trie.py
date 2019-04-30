import unittest
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.words = []
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            cur.words.append(word)

    def getWords(self, prefix):
        cur = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return []
            cur = cur.children[idx]
        return cur.words

class TryTrie:
    def getCommonPrefixWords(self, words, prefix):
        trie = Trie()
        for w in words:
            trie.addWord(w)
        return trie.getWords(prefix)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(TryTrie().getCommonPrefixWords(['hello', 'heello', 'hellllp'], 'hel'), ['hello', 'hellllp'])

if __name__ == "__main__":
    unittest.main()