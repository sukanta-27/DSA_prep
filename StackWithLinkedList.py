class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, size=100):
        self.top = None
    
    def isEmpty(self):
        if self.top == None:
            return True
        return False

    def display(self):
        # if self.isEmpty:
        #     print("Stack is Empty")
        #     return
        
        curr = self.top
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

        print()
        return

    def push(self, data):
        node = Node(data)
        if node is None:
            print("Stack Overflow")
            return
        node.next = self.top
        self.top = node

    def pop(self):
        if self.isEmpty():
            print("List is empty")
            return
        
        temp = self.top.data
        self.top = self.top.next
        return temp
    
    def peek(self):
        if self.isEmpty():
            print("List is empty")
            return
        
        return self.top.data

s = Stack(1)
s.push(1)
s.display()
s.push(2)
s.display()
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
s.pop()
