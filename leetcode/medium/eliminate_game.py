class Solution(object):
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