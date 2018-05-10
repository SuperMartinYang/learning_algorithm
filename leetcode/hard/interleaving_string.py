class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [set() for _ in range(len(s3) + 1)]
        dp[0] = {'0' + '|' + '0'}
        for i in range(len(s3)):
            if not dp[i]:
                return False
            for pos in dp[i]:
                pos = list(map(int, pos.split('|')))
                if pos[0] < len(s1) and s1[pos[0]] == s3[i]:
                    dp[i + 1].add(str(pos[0] + 1) + '|' + str(pos[1]))
                if pos[1] < len(s2) and s2[pos[1]] == s3[i]:
                    dp[i + 1].add(str(pos[0] + '|' + str(pos[1] + 1)))
        if not dp[len(s3)]:
            return False
        return True

print(Solution().isInterleave("a", "", "c"))