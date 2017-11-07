class Trie(object):
    def __init__(self, key=None):
        """
        Initialize your data structure here.
        """
        self.key = key
        self.children = []
        self.end = None  # 1: end, 0: not end

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self
        len_word = len(word)
        j = 0
        while j < len_word:
            len_child = len(cur.children)
            i = 0
            while i < len_child:
                if word[j] == cur.children[i].key:
                    cur = cur.children[i]
                    break
                i += 1
            if i == len_child:
                for k in range(j, len_word):
                    len_cur = len(cur.children)
                    cur.children.append(Trie(word[k]))
                    cur = cur.children[len_cur]
                break
            j += 1
        cur.end = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        len_word = len(word)
        cur = self
        j = 0
        while j < len_word:
            len_child = len(cur.children)
            i = 0
            while i < len_child:
                if word[j] == cur.children[i].key:
                    cur = cur.children[i]
                    break
                i += 1
            if i == len_child:
                return False
            j += 1
        if cur.end == 1:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        len_prefix = len(prefix)
        cur = self
        j = 0
        while j < len_prefix:
            len_child = len(cur.children)
            i = 0
            while i < len_child:
                if prefix[j] == cur.children[i].key:
                    cur = cur.children[i]
                    break
                i += 1
            if i == len_child:
                return False
            j += 1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)