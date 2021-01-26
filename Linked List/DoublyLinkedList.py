class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        temp = Node(data)
        
        if not self.head:
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insert_at_end(self, data):
        temp = Node(data)

        if not self.head:
            self.head = temp
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next

            curr.next = temp
            temp.prev = curr

    def insert_before(self, data, before):
        node = Node(data)

        if not self.head:
            self.head = node
        elif self.head.data == before:
            self.insert(data)
        else:
            curr = self.head

            while(curr):
                if curr.data == before:
                    curr.prev.next = node
                    node.prev = curr.prev
                    node.next = curr
                    curr.prev = node

                curr = curr.next


    def delete(self, data):
        """
            4 scenarios:
                1. Delete from beginning
                2. Delete from end
                3. Delete only item
                4. Delete from middle
        """
        print(f"Deleting {data}")
        curr = self.head
        if curr:
            while curr:
                if curr.data == data:
                    if not curr.prev and curr.next:
                        # First element
                        curr.next.prev = None
                        self.head = curr.next
                        return
                    elif curr.prev and not curr.next:
                        # Last element
                        curr.prev.next = None
                        return
                    elif not curr.prev and not curr.next:
                        # Only element
                        self.head = None
                        return
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        return
                curr = curr.next
        print("Element not found")

    def print(self):
        if not self.head:
            print("....")
        curr = self.head

        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        
        print()
        return


dll = DLL()
dll.insert(10) # 10
dll.print()
dll.delete(10) # ..
dll.print()
dll.delete(10) # Element not found
dll.insert(10) # 10
dll.insert(20) # 20 10
dll.insert(30) # 30 20 10
dll.insert_at_end(40) # 30 20 10 40
dll.insert_before(50, 40) # 30 20 10 50 40
dll.insert_before(60, 30) # 60 30 20 10 50 40
dll.insert_before(70, 10) # 60 30 20 70 10 50 40
dll.delete(40) # 60 30 20 70 10 50
dll.print()
dll.delete(70) # 60 30 20 10 50
dll.print()