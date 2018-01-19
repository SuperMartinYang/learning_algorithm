class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        # init
        p_dict = {}
        for i in p:
            p_dict[i] = p_dict[i] + 1 if i in p_dict else 1

        s_dict = {}
        for i in range(len(p)):
            s_dict[s[i]] = s_dict[s[i]] + 1 if s[i] in s_dict else 1
        result_list = []

        # useful func
        def add(new_char):
            s_dict[new_char] = s_dict[new_char] + 1 if new_char in s_dict else 1

        def minus(old_char):
            s_dict[old_char] -= 1
            if s_dict[old_char] == 0:
                del s_dict[old_char]

        # solve
        for i in range(len(p), len(s)):
            if s_dict == p_dict:
                result_list.append(i - len(p))
            add(s[i])
            minus(s[i - len(p)])
        if s_dict == p_dict:
            result_list.append(len(s) - len(p))
        return result_list

s = Solution()
print(s.findAnagrams('cbaebabacd', 'abc'))