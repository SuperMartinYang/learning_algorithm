class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        x, y, z = 0, 1, 2
        result = []
        hash_p = self.hash(p)
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return []
        for i in range(0, len_s - len_p + 1):
            if self.hash(s[i:i + len_p]) == hash_p :
                result.append(i)
        return result


    def hash(self, p):
        hs_tb = {}
        for i in p:
            if i not in hs_tb.keys():
                hs_tb[i] = 1
            else:
                hs_tb[i] += 1
        return hs_tb
