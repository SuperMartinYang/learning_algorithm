class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2: return 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        if len(num2) == 1:
            carry = 0
            res = ''
            i = 0
            n2 = int(num2)
            while i < len(num1):
                tmp = n2 * int(num1[len(num1) - i - 1]) + carry
                res = str(tmp % 10) + res
                carry = tmp // 10
                i += 1
            if carry: res = str(carry) + res
            return res
        # divid and conquer
        h1 = len(num1) // 2
        l1 = num1[:h1]
        r1 = num1[h1:]
        h2 = len(num2) // 2
        l2 = num2[:h2]
        r2 = num2[h2:]
        hh = self.multiply(l1, l2) + '0' * (len(num1) + len(num2) - h1 - h2)
        hl = self.multiply(l1, r2) + '0' * (len(num1) - h1)
        lh = self.multiply(r1, l2) + '0' * (len(num2) - h2)
        ll = self.multiply(r1, r2)

        res = self.add(self.add(ll, lh), self.add(hh, hl))
        return res

    def add(self, num1, num2):
        carry = 0
        i = 0
        res = ''
        while i < len(num1) or i < len(num2):
            # get num
            tmp = 0
            if i < len(num1): tmp += int(num1[len(num1) - i - 1])
            if i < len(num2): tmp += int(num2[len(num2) - i - 1])
            # add
            tmp += carry
            new_int = tmp % 10
            # carry, update
            carry = tmp // 10
            res = str(new_int) + res
            i += 1
        if carry: res = str(carry) + res
        return res

print(Solution().multiply('123', '456'))
# print(Solution().add('123', '456'))
