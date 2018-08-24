class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 pointer
        alp_idx = [-1] * 256      # last appear idx
        i, j = 0, 0
        cnt = 0
        while j < len(s):
            dif = ord(s[j])
            if alp_idx[dif] != -1:
                cnt = max(cnt, j - i)
                while i < alp_idx[dif] + 1:
                    alp_idx[ord(s[i])] = -1
                    i += 1

            alp_idx[dif] = j
            j += 1
        cnt = max(cnt, j - i)
        return cnt

print(Solution().lengthOfLongestSubstring('pwwkew'))