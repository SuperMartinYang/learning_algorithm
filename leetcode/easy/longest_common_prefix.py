class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        str_rdm = strs[0]
        longest_prefix = ''
        for i in range(len(str_rdm)):
            for item in strs:
                if i >= len(item) or str_rdm[i] != item[i]:
                    return  longest_prefix
            longest_prefix += str_rdm[i]
        return longest_prefix

s = Solution()
print(s.longestCommonPrefix(['aa','a']))