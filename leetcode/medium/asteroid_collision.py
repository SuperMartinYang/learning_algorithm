class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if not stack or a * stack[-1] > 0 or (stack[-1] < 0 and a > 0):
                stack.append(a)
            else:
                while stack and a * stack[-1] < 0 and abs(a) > abs(stack[-1]):
                    stack.pop()
                if stack and a == -stack[-1]:
                    stack.pop()
                    continue
                if not stack or a * stack[-1] > 0:
                    stack.append(a)
            print(stack)
        return stack


Solution().asteroidCollision([-2,1,-1,-3])