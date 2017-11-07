class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        Given a string, find the length of the longest substring without repeating characters.
        Examples:
        Given "abcabcbb", the answer is "abc", which the length is 3.
        Given "bbbbb", the answer is "b", with the length of 1.
        Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
        :param s: str
        :return: int
        """
        str = ''
        length = 0
        longest_len = 0
        for i in s:
            if i in str:
                if length > longest_len:
                    longest_len = length
                index = str.index(i)
                str = str[index+1:]+i
                length -= index
            else:
                str += i
                length += 1

        return max(longest_len,length)

a = Solution()
print(a.lengthOfLongestSubstring('ggububgvfk'))

