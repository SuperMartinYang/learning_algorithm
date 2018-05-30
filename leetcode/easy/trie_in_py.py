def form_trie(words):
    root = {}
    for word in words:
        cur = root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['#'] = '#'
    return root
