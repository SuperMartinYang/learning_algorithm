class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def stringAdd(s1, s2):
            # len1 > len2
            carry = 0
            len1 = len(s1)
            len2 = len(s2)
            newStr = ''
            for i in range(len1):
                tmp = int(s1[len1 - i - 1]) + int(s2[len2 - i - 1]) + carry if i < len2 else int(
                    s1[len1 - i - 1]) + carry
                rem = tmp % 10
                carry = tmp // 10
                newStr = str(rem) + newStr
            if carry != 0:
                newStr = str(carry) + newStr
            return newStr

        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if i > 1 and num[0] == '0' or j - i > 1 and num[i] == '0':
                    return False
                tmp = stringAdd(num[:i], num[i: j])
                lentmp = len(tmp)
                if len(num) - j < lentmp or tmp != num[j: j + lentmp]:
                    break
                else:
                    if self.isAdditiveNumber(num[i + 1:]):
                        return True
                    break
        return False

        for i in range(1, len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                tmp = stringAdd(num[:i], num[i: j])
                lentmp = len(tmp)
                if len(num) - j < lentmp or tmp != num[j: j + lentmp]:
                    break
                elif tmp == num[j: j + lentmp]:
                    if self.isAdditiveNumber(num[i:]):
                        return True
                    break
        return False

s = Solution()
print s.isAdditiveNumber("112358")