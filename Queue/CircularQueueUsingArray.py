class CircularQueue:

    def __init__(self, size=5):
        self.queue = [None]*size
        self.head = self.rear = -1
        self.size = size
    
    def isEmpty(self):
        return self.head == -1

    def enqueue(self, data):
        if self.rear == -1:
            self.rear = self.head = 0
            self.queue[self.rear] = data
            return
        else:
            x = (self.rear + 1)%self.size
            if self.queue[x] == None and x != self.head:
                self.queue[x] = data
                self.rear = x
            elif x == self.head:
                print("Queue is full at the moment")
                return


    def dequeue(self):
        if self.head == -1:
            print("Queue is Empty")
            return

        
        temp = self.queue[self.head]
        self.queue[self.head] = None
        if self.head == self.rear:
            self.head = self.rear = -1
            return temp
        self.head = (self.head + 1)%self.size
        return temp

    def __repr__(self):
        if self.isEmpty():
            return "Nothing to print"
        result = ""
        x = self.head
        y = self.rear

        while x <= y:
            result += str(self.queue[x]) + " "
            x += 1
        return result


q = CircularQueue(4)
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