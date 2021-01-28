class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularQueue:
    def __init__(self):
        self.head = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if not self.rear:
            # List is empty
            self.head = node
            self.head.next = self.head
            self.rear = self.head
            return
        
        else:
            node.next = self.head
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.head:
            print("Queue Empty")
            return
        
        temp = self.head
        if self.head == self.rear:
            # Last element
            self.head = self.rear = None
        else:
            self.head = self.head.next
            self.rear.next = self.head
        return temp.data

    def __str__(self):
        if not self.head:
            return "Empty Queue"
        curr = self.head
        result = ""
        while True:
            result += str(curr.data) + " "
            if curr.next == self.head:
                break
            curr = curr.next
        return result


q = CircularQueue()
q.enqueue(1)
print("Deque: ",q.dequeue())
print(q)
print("Deque: ",q.dequeue())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print("Deque: ",q.dequeue())
print(q)
print("Deque: ",q.dequeue())
print(q)