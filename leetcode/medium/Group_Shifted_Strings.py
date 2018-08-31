import collections
class Solution(object):
    def group_shifted_strings(self, words):
        dic = collections.defaultdict(list)
        for w in words:
            dis = (ord(w[0]) - ord('a')) % 26
            key = ''
            for ch in w:
                key += chr((ord(ch) - dis) % 26)
            dic[key].append(w)
        return dic.values()

print(Solution().group_shifted_strings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))