class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insert_before_given_item(self, data, item=None):
        node = Node(data)
        if not item:
            self.insert_at_beginning(data)
        elif not self.head:
            self.head = node
        else:
            curr = self.head
            prev = None

            while(curr.data != item):
                prev = curr
                curr = curr.next
            
            node.next = curr
            if prev:
                prev.next = node
            else:
                self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next

            curr.next = node
    
    def delete_item(self):
        pass

    def delete_index(self):
        pass

    def reverse(self):
        pass

    def print(self):
        if not self.head:
            print("The List is empty")
        else:
            curr = self.head
            while curr:
                print(curr.data, end=" ")
                curr = curr.next
            print()



LL = LinkedList()
LL.insert_at_beginning(10)
LL.insert_at_beginning(20)
LL.insert_at_beginning(30)
LL.insert_at_end(40)
LL.insert_before_given_item(50, 40)
LL.insert_before_given_item(1, 30)
LL.insert_before_given_item(2, 10)
LL.print()