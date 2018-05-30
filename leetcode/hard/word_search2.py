class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        if not board or not words:
            return []
        m = len(board)
        n = len(board[0])

        used = [[False for _ in range(n)] for _ in range(m)]
        res = []
        words = set(words)

        # form trie
        root = {}
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['#'] = '#'

        def dfs(i, j, word, node, path):
            if '#' in node:
                res.append(word)
                words.remove(word)
                cur = node
                del cur['#']
                if not cur:
                    while path and not cur:
                        cur, curl = path.pop()
                        del cur[curl]
                    return
            if not words:
                return
            used[i][j] = True
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if -1 < x < m and -1 < y < n and not used[x][y] and board[x][y] in node:
                    dfs(x, y, word + board[x][y], node[board[x][y]], path + [[node, board[x][y]]])
            used[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, board[i][j], root[board[i][j]], [[root, board[i][j]]])
        return res

Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"])