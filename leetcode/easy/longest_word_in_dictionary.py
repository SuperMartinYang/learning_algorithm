class Solution(object):
    def longestWord2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dic = set(words)
        words.sort(key=lambda c: (-len(c), c))  # O(nlogn)
        for w in words:
            i = 1
            while i < len(w):
                if w[:len(w) - i] not in dic:
                    break
                i += 1
            if i == len(w):
                return w
        return ''

    def longestWord(self, words):
        root = {}
        root['#'] = '#'
        ml = 0
        res = ''
        for w in words:
            cur = root
            for ch in w:
                if ch in cur:
                    cur = cur[ch]
                else:
                    cur[ch] = {}
                    cur = cur[ch]
            cur['#'] = '#'
        # bfs
        level = [root]
        while level:
            tmp = []
            for cur in level:
                for key in cur.keys():
                    if key != '#' and '#' in cur[key]:
                        tmp.append(cur[key])
            if not tmp: return level[0]
            level = tmp

        return ''

print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))