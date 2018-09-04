class WordFilter(object):

    def __init__(self, words):
        """
        two tie
        :type words: List[str]
        """
        self.pre_trie = {}
        self.suf_trie = {}
        for idx, w in enumerate(words):
            pre_cur = self.pre_trie
            suf_cur = self.suf_trie
            for i in range(len(w)):
                if w[i] not in pre_cur:
                    pre_cur[w[i]] = {}
                pre_cur = pre_cur[w[i]]
                if w[len(w) - 1 - i] not in suf_cur:
                    suf_cur[w[len(w) - 1 - i]] = {}
                suf_cur = suf_cur[w[len(w) - 1 - i]]
            pre_cur['#'] = w  # store the word and weight
            suf_cur['#'] = w

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        # from prefix, use BFS to search which is ended with suffix, m
        cur = self.trie
        level = [cur[prefix[0]]]
        # TODO
        return