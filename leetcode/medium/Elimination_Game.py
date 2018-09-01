class Solution(object):
    def elimination_game(self, n):
        return 1 if n == 1 else 2 * (1 + n // 2 - self.elimination_game(n // 2))

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = True
        step = 1
        head = 1
        remain = n
        while remain > 1:
            if left or remain % 2 == 1:
                head += step
            step *= 2
            left = not left
            remain //= 2
        return head

print(Solution().elimination_game(9))