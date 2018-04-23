class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        res = ''
        allNode = path.split('/')
        # a . .. ''
        for n in allNode:
            if n == '..':
                if stack:
                    stack.pop()
            elif n != '.' and n != '':
                stack.append(n)
        if not stack:
            res = '/'
        while stack:
            res = '/' + stack.pop() + res
        return res
s = Solution()
print(s.simplifyPath('/home/'))