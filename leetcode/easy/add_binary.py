class Solution(object):
    def addBinary(self, a, b):
        """
        For example,
        a = "11"
        b = "1"
        Return "100".

        :type a: str
        :type b: str
        :rtype: str
        """
        alen = len(a)
        blen = len(b)
        if alen < blen:
            a, b, alen, blen = b, a, blen, alen
        result = ''
        carr = ''
        for i in range(0, alen):
            if i < blen:
                if a[- i - 1] == '1' and b[- i - 1] == '1':
                    if carr == '1':
                        result = '1' + result
                        carr == 0
                    else:
                        result = '0' + result
                        carr = '1'
                elif a[-i - 1] == '1' or b[-i - 1] == '1':
                    if carr == '1':
                        result = '0' + result
                        carr = '1'
                    else:
                        result = '1' + result
                else:
                    if carr == '1':
                        result = '1' + result
                        carr = '0'
                    else:
                        result = '0' + result
            else:
                if carr == '1' and a[-i - 1] == '1':
                    result = '0' + result
                    carr = '1'
                elif carr == '1' or a[-i -1] == '1':
                    result = '1' + result
                    carr = '0'
                else:
                    result = '0' + result
        if carr == '1':
            result = carr + result
        return result

    def addBinary2(self, a, b):
        # TODO: code optimize, while (i > 0 || j > 0) if i > 0: ... if j > 0: ...
        carry = 0
        i = 0
        res = ''
        while i < len(a) and i < len(b):
            # get num
            int1 = int(a[len(a) - i - 1])
            int2 = int(b[len(b) - i - 1])
            # add
            tmp = int1 + int2 + carry
            new_int = tmp % 2
            # carry, update
            carry = tmp // 2
            res = str(new_int) + res
            i += 1
        if i == len(a) and i == len(b):
            if carry: res = str(carry) + res
            return res
        elif i == len(a):
            while i < len(b):
                int2 = int(b[len(b) - i - 1])
                tmp = int2 + carry
                new_int = tmp % 2
                carry = tmp // 2
                res = str(new_int) + res
                i += 1
            if carry: res = str(carry) + res
            return res
        else:
            while i < len(a):
                int1 = int(a[len(a) - i - 1])
                tmp = int1 + carry
                new_int = tmp % 2
                carry = tmp // 2
                res = str(new_int) + res
                i += 1
            if carry: res = str(carry) + res
            return res
        return res

s = Solution()
# result = s.addBinary('1010','1011')
result = s.addBinary2('11', '1')
print(result)

