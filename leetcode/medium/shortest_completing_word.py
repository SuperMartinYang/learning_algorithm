import collections
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        target = collections.defaultdict(int)
        for ch in licensePlate:
            if ch.isalpha():
                target[ch.lower()] += 1
        # return target.items()
        res = ''
        shortest = 1e9
        for w in words:
            cnt = 0
            wd = collections.defaultdict(int)
            tried = set()
            for ch in w:
                ch = ch.lower()
                if ch in target and ch not in tried:
                    wd[ch] += 1
                    if wd[ch] >= target[ch]:
                        cnt += 1
                        tried.add(ch)
            if cnt == len(target) and len(w) < shortest:
                res = w
        return res

print(Solution().shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))