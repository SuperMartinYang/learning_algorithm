class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_rev = s[::-1]
        now_same = ''
        longest_same = ''
        start = longest = long_ = longest_start = longest_stop = 0
        len_ = len(s)
        for i in range(len_):
            if s[i] == s_rev[-i -1]:
                long_ += 1
            elif long_ != 0:
                stop = i
                start = stop - long_
                if long_ > longest and self.valid_palin(s, start, stop):
                    longest = long_
                    longest_start = start
                    longest_stop = stop
                long_ = 0
        return s[longest_start: longest_stop]
    def valid_palin(self, s, longest_start, longest_stop):
        # check whether in s there are the same str in the rev posi
        for i in range(longest_start, longest_stop):
            if s[i] != s[-i - 1]:
                return True
        return False
s = Solution()
print(s.longestPalindrome('babad'))