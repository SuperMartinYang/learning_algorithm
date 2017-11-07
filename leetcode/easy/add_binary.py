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


s = Solution()
result = s.addBinary('1010','1011')
print(result)
