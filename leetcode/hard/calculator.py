class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

        # A utility function to check is the given character

    # is operand
    def isOperand(self, ch):
        return ch.isdigit()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
        i = 0
        # Iterate over the expression for conversion
        while i < len(exp):
            # If the character is an operand,
            # add it to output
            if self.isOperand(exp[i]):
                start = i
                while i < len(exp) and self.isOperand(exp[i]):
                    i += 1
                self.output.append(exp[start:i])
                continue

            # If the character is an '(', push it to stack
            elif exp[i] == '(':
                self.push(exp[i])

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif exp[i] == ')':
                while ((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # space
            elif exp[i] == ' ':
                i += 1
                continue

            # An operator is encountered
            else:
                while (not self.isEmpty() and self.notGreater(exp[i])):
                    self.output.append(self.pop())
                self.push(exp[i])
            i += 1

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        return " ".join(self.output)


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = Conversion(1000).infixToPostfix(s).split()
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] in ('-', '+'):
                op2 = stack.pop()
                op1 = stack.pop()
                if s[i] == '+':
                    stack.append(op1 + op2)
                else:
                    stack.append(op1 - op2)
            else:
                stack.append(int(s[i]))
        return stack.pop()


print(Solution().calculate("123"))
