class Conversion:

    def __init__(self):
        self.stack = []
        self.precedence = {
            '(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

    def greaterThanOrEqualToTop(self, operator):
        # Checks if the operator in greater in terms of precedence or not compared to the top element
        if self.precedence[self.stack[-1]] < self.precedence[operator]:
            return True
        return False

    def infixToPostfix(self, expression):
        result = []
        for i in expression:
            # print(self.stack)
            if i.isalnum():
                result.append(i)
            elif i == '(':
                self.stack.append(i)
            elif i == ')':
                while len(self.stack) > 0 and self.stack[-1] != '(':
                    result.append(self.stack.pop())
                if self.stack[-1] == '(':
                    self.stack.pop()
            else:
                if len(self.stack) > 0 and not self.greaterThanOrEqualToTop(i):
                    while len(self.stack) > 0 and not self.greaterThanOrEqualToTop(i):
                        result.append(self.stack.pop())
                    self.stack.append(i)
                else:
                    self.stack.append(i)
        
        while len(self.stack) > 0:
            x = self.stack.pop()
            result.append(x)
        
        postfix = ''.join(result)
        print(f"Infix: {expression} \t Postfix: {postfix}")
        return postfix

    def infixToPrefix(self, expression):
        reverse_expression = []

        for i in reversed(expression):
            if i == ')':
                reverse_expression.append('(')
            elif i == '(':
                reverse_expression.append(')')
            else:
                reverse_expression.append(i)

        postfix = self.infixToPostfix("".join(reverse_expression))
        prefix = postfix[::-1]

        print(f"Infix: {expression} \t Prefix: {prefix}")
        return prefix

c = Conversion()
c.infixToPostfix("2+3*4+5+6")
c.infixToPostfix("(2+3*4+(5+6))")

c.infixToPrefix("2+3*4+5+6")
c.infixToPrefix("(2+3*4+(5+6))")
c.infixToPrefix("A+B*C/(E-F)")


