class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']
        alpha_d = [0 for _ in range(26)]
        res = []
        # form dict
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            alpha_d[idx] += 1

        def alter_d(ss, is_add):
            tmp = [0 for _ in range(26)]
            for i in range(len(ss)):
                idx = ord(ss[i]) - ord('a')
                tmp[idx] += 1

            for ch in ss:
                if is_add:
                    break
                idx = ord(ch) - ord('a')
                if alpha_d[idx] >= tmp[idx]:
                    continue
                return False
            for ch in ss:
                idx = ord(ch) - ord('a')
                if is_add:
                    alpha_d[idx] += 1
                else:
                    alpha_d[idx] -= 1
            return True

        def backtracking(p_s):
            if sum(alpha_d) == 0:
                res.append(p_s)
                return True
            for i in range(len(nums)):
                if not alter_d(nums[i], False):
                    continue
                if backtracking(p_s + str(i)):
                    return True
                alter_d(nums[i], True)
            return False

        backtracking('')
        return res[0]


print(Solution().originalDigits('zeroonetwothreefourfivesixseveneightnine'))
# print(Solution().originalDigits('zerooneoneoneonefivefivesixsixeightthree'))