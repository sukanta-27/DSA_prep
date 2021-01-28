class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # print("Hi", data)
        node = Node(data)
        if not node:
            print("Stack Overflow")
            return
        if not self.head and not self.tail:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if not self.head:
            print("Queue is empty")
            return
        else:
            temp = self.head
            self.head = temp.next
            if not self.head:
                self.tail = None
        return temp.data

    def __str__(self):
        curr = self.head
        string = ""
        while curr:
            string += str(curr.data) + " "
            curr = curr.next
        return string


q = Queue()
q.enqueue(1)
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
q.dequeue()
print(q)