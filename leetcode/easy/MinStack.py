class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.size += 1

    def pop(self):
        """
        :rtype: void
        """
        self.size -= 1
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.size - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

s = MinStack()
s.push(9)
s.push(0)
s.push(-4)

print(s.pop())
print(s.getMin())
print(s.top())
