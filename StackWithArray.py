class Stack:
    def __init__(self, size=100):
        self.top = -1
        self.stack = [None]*size
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isFull(self):
        if self.top == len(self.stack)-1:
            return True
        return False

    def display(self):
        if not self.isEmpty():
            i = 0
            while i <= self.top:
                print(self.stack[i], end=" ")
                i += 1
            print()
        else:
            print("Stack is empty")

    def push(self, data):
        if not self.isFull():
            print(f"Pushing {data} into the stack")
            self.top += 1
            self.stack[self.top] = data
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():
            temp = self.stack[self.top]
            self.top -= 1
            return temp
        else:
            print("Stack underflow")
    def peek(self):
        if not self.isEmpty():
            temp = self.stack[self.top]
            return temp
        else:
            print("Stack underflow")

s = Stack(1)
s.push(1)
s.push(2)
s.display()
print("Peek: ", s.peek())
print("Pop: ", s.pop())
s.push(3)
s.display()
print("Pop: ", s.pop())
s.display()
s.pop()
s.display()
s.pop()