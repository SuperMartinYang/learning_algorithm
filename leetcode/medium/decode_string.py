class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(ss):
            res = ''
            i = 0
            length = 0
            while i < len(ss):
                if ss[i].isdigit():
                    n = 1
                    while i + n < len(ss) and ss[i + n].isdigit():
                        n += 1
                    subres = helper(ss[i + n + 1:])
                    res += int(ss[i:i + n]) * subres[0]
                    length += n + subres[1] + 1
                    i += n + subres[1] + 1
                elif ss[i].isalpha():
                    res += ss[i]
                    length += 1
                    i += 1
                elif ss[i] == ']':
                    return [res, length + 1]
            return [res, length]
        return helper(s)[0]

print(Solution().decodeString("12[abc]3[cd]ef"))