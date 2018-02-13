class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # keep adding words and 1 space for each
        # if length greater than L, less word, do justify
        def justify(start, stop, wordLenWithSpace):
            if start == stop:
                return words[start] + ' ' * (maxWidth - len(words[start]))
            s = ''
            space = (maxWidth - (wordLenWithSpace - (stop - start + 1))) // (stop - start)
            remainSpace = maxWidth - (stop - start) * space - wordLenWithSpace
            for i in range(start, stop):
                if i <= start + remainSpace:
                    s += words[i] + ' ' * (space + 1)
                else:
                    s += words[i] + ' ' * space
            s += words[stop]
            return s

        pre = 0
        start = 0
        res = []
        for i in range(len(words)):
            if len(words[i]) + pre > maxWidth:
                res.append(justify(start, i - 1, pre))
                start = i
                pre = len(words[i]) + 1
            else:
                pre += len(words[i]) + 1
        if pre:
            res.append(justify(start, len(words) - 1, pre))
        return res if res else [""]

print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))