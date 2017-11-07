class Solution(object):
    def romanToInt(self, s):
        """
        Roman number is read from left to right
        I = 1	V = 5	X = 10
        L = 50	C = 100	D = 500
        M = 1000

        MMMCDVIII

        CM
        C
        CD
        DC|C|C

        XC
        LX
        XL
        CX

        3408
        :type s: str
        :rtype: int
        """
        pair = {'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1}
        sum = 0
        for i in range(len(s)):
            if i == 0:
                if i == (len(s) - 1):
                    return pair[s[i]]
                if pair[s[i]] < pair[s[i+1]]:
                    sum -= pair[s[i]]
                else:
                    sum += pair[s[i]]
            elif i == (len(s) - 1):
                sum += pair[s[i]]
            elif (pair[s[i-1]] >= pair[s[i]] and pair[s[i]] >= pair[s[i+1]]) or (pair[s[i-1]] < pair[s[i]] and pair[s[i]] > pair[s[i+1]]):
                sum += pair[s[i]]
            elif pair[s[i-1]] > pair[s[i]] and pair[s[i]] < pair[s[i+1]]:
                sum -= pair[s[i]]

        return sum
s = Solution()
print(s.romanToInt("M"))