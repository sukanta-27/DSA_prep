class Evaluate:

    def __init__(self):
        self.stack = []

    def evaluatePostfix(self, expression):

        for i in expression:
            if i.isnumeric():
                self.stack.append(int(i))
            else:
                if len(self.stack) >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if i == '+':
                        self.stack.append(a+b)
                    elif i == '-':
                         self.stack.append(b-a)
                    elif i == '*':
                         self.stack.append(a*b)
                    elif i == '/':
                         self.stack.append(b/a)
            # print(f"Stack state at char {i} is {self.stack}")
        return self.stack.pop()
                     
    def evaluatePrefix(self, expression):
        for i in reversed(expression):
            if i.isnumeric():
                self.stack.append(int(i))
            else:
                if len(self.stack) >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if i == '+':
                        self.stack.append(a+b)
                    elif i == '-':
                        # As the ordering will change in reverse, we need to keep that in mind before
                        # calculating - and /. Because of this here we will need to calculate
                        # a - b instead of b-a. Similar logic applies in case of division.
                         self.stack.append(a-b)
                    elif i == '*':
                         self.stack.append(a*b)
                    elif i == '/':
                         self.stack.append(a/b)
            # print(f"Stack state at char {i} is {self.stack}")
        return self.stack.pop()


e = Evaluate()
print("Postfix evaluation: ")
print(e.evaluatePostfix("2362/*+6+3-"))
print(e.evaluatePostfix("23+4+63/-"))

print("Prefix evaluation: ")
print(e.evaluatePrefix("+2+3-4/63"))

