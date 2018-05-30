class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        use stack, and arr to store ch frequency
        :type s: str
        :rtype: str
        """
        stack = []
        freq = [0 for _ in range(26)]
        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1

        for ch in s:
            freq[ord(ch) - ord('a')] -= 1
            if ch in stack:
                continue
            while stack and freq[ord(stack[-1]) - ord('a')] > 0 and ch < stack[-1]:
                stack.pop()
            stack.append(ch)
        return ''.join(stack)

print(Solution().removeDuplicateLetters('cabacdcbc'))