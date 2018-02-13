class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def valid(s):
            stack = []
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(s[i])
                elif s[i] == ')':
                    if not stack:
                        return False
                    stack.pop()
                else:
                    continue
            if stack:
                return False
            else:
                return True

        if valid(s):
            return [s]
        level = 0
        dic = {0: [s]}
        while dic[level]:
            level += 1
            dic[level] = []
            result = set()
            for s_tmp in dic[level - 1]:
                cur = []
                for i in range(len(s_tmp)):
                    new_s = s_tmp[:i] + s_tmp[i + 1:]
                    if valid(new_s):
                        result.add(new_s)
                    cur.append(new_s)
                dic[level].extend(cur)
            if result != set():
                return list(result)


s = Solution()
print(s.removeInvalidParentheses("()(((((((()"))