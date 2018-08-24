import collections
import copy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words: return []
        finW = collections.defaultdict(int)
        cnt = len(words)
        wl = len(words[0])
        for w in words:
            finW[w] += 1
            if len(w) != wl: return []
        res = []
        for i in range(0, wl):      # for some case start from s % wl != 0
            k = i
            j = i
            dicW = collections.defaultdict(int)
            count = 0
            while j <= len(s) - wl:
                ss = s[j:j + wl]
                if ss in finW:
                    dicW[ss] += 1
                    if dicW[ss] <= finW[ss]:
                        count += 1
                    else:   # too many ss, forward k to erase
                        while dicW[ss] > finW[ss]:
                            # forward k, ning que wu lan
                            ss1 = s[k:k + wl]
                            dicW[ss1] -= 1
                            if dicW[ss1] < finW[ss1]: count -= 1
                            k += wl
                    if count == cnt:
                        # result get
                        res.append(k)
                        dicW[s[k:k + wl]] -= 1
                        count -= 1
                        k += wl
                else:   # not a word when processing
                    dicW = collections.defaultdict(int)
                    count = 0
                    k = j + wl
                j += wl
        return res

print(Solution().findSubstring("abaababbaba", ["ba","ab","ab"]))
print(Solution().findSubstring("barfoogfoobarthefoobarman", ["bar","foo","the"]))
print(Solution().findSubstring('foobarthebarfooman', ['foo', 'bar']))
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
# print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))