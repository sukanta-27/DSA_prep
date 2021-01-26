class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class CDLL:
    def __init__(self):
        self.head = None

    def print(self):
        if not self.head:
            print("List is Empty")

        else:
            curr = self.head
            while True:
                print(curr.data, end=" ")
                curr = curr.next
                if curr == self.head: # Pointer is again at the first element
                    break
            print()

    def getLastNode(self):

        if not self.head:
            return
        curr = self.head
        while True:
            if curr.next == self.head:
                break
            curr = curr.next

        return curr

    def insert_at_beginning(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.head.prev = node
            self.head.next = node
        else:
            last = self.getLastNode()
            node.next = self.head
            node.prev = last
            self.head.prev = node
            last.next = node
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.head.prev = node
            self.head.next = node
        else:
            last = self.getLastNode()
            node.prev = last
            self.head.prev = node
            node.next = self.head
            last.next = node

    def insert_after(self, data, item):
        node = Node(data)
        if not self.head:
            self.head = node
            self.head.prev = node
            self.head.next = node
        else:
            curr = self.head
            while True:
                if curr.data == item:
                    curr.next.prev = node
                    node.next = curr.next
                    node.prev = curr
                    curr.next = node
                    break

                if curr.next == self.head:
                    print("Item not found")
                    break
                curr = curr.next                  

    def delete(self, item):
        if not self.head:
            print("List is Empty")
        
        curr = self.head
        last = self.getLastNode()
        while True:
            if curr.data == item:
                if curr.prev == last:
                    # Delete first element
                    if curr.next == self.head:
                        # Only one element in the list
                        self.head = None
                        return
                    else:
                        # More than one element in the list
                        curr.next.prev = last
                        last.next = curr.next
                        self.head = curr.next
                        return
                elif curr.next == self.head:
                    # Last element to be deleted
                    curr.prev.next = self.head
                    self.head.prev = curr.prev
                    return
                else:
                    # Any middle element to be deleted
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    return
            
            if curr.next == self.head:
                break
            curr = curr.next
        
        print("Element not found")
        return
ll = CDLL()

ll.insert_at_beginning(1)
ll.print()
ll.delete(1)
ll.print()
ll.insert_at_beginning(1)
ll.print()
ll.insert_at_beginning(2)
ll.print()
ll.insert_at_beginning(3)
ll.print()
ll.insert_at_end(4)
ll.print()
ll.insert_after(5, 3) # 3 5 2 1 4
ll.print()
ll.insert_after(6, 2) # 3 5 2 6 1 4
ll.print()
ll.insert_after(7, 4) # 3 5 2 6 1 4 7
ll.print()
ll.insert_after(12, 33) # Item not found
ll.delete(55) # Element not found
ll.delete(6) # 3 5 2 1 4 7
ll.print()
ll.delete(7) # 3 5 2 1 4
ll.print()
