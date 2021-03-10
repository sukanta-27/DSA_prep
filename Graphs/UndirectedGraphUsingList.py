class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Graph:

    def __init__(self, numberOfVertices):
        self.adjacency_list = [None]*numberOfVertices
        self.numberOfVertices = numberOfVertices

    def isEdgePresent(self, source, destination):
        isAlreadyPresent = False
        nodes = self.adjacency_list[source]
        while nodes:
            if nodes.data == destination:
                isAlreadyPresent = True
                break
            nodes = nodes.next
        
        return isAlreadyPresent

    def add_edge(self, source, destination):
        if source < 0 or source >= self.numberOfVertices or destination < 0 or destination >= self.numberOfVertices:
            print("Invalid Source or Destination given")
            return        

        if not self.isEdgePresent(source, destination):
            node = Node(destination)
            node.next = self.adjacency_list[source]
            self.adjacency_list[source] = node

            node = Node(source)
            node.next = self.adjacency_list[destination]
            self.adjacency_list[destination] = node
        else:
            print("Edge already present between {} and {}".format(source, destination))

    def remove_edge(self, source, destination):
        if source < 0 or source >= self.numberOfVertices or destination < 0 or destination >= self.numberOfVertices:
            print("Invalid Source or Destination given")
            return None

        if not self.isEdgePresent:
            print("No edge is present between {} and {}".format(source, destination))
            return None     
        else:
            node = self.adjacency_list[source]
            prev = None

            while node:
                if node.data == destination:
                    if prev:
                        prev.next = node.next
                    else:
                        self.adjacency_list[source] = node.next
                    break
                prev = node
                node = node.next

            node = self.adjacency_list[destination]
            prev = None

            while node:
                if node.data == source:
                    if prev:
                        prev.next = node.next
                    else:
                        self.adjacency_list[destination] = node.next
                    break
                prev = node
                node = node.next
        
        return

    def display_graph(self):
        for i in range(self.numberOfVertices):
            firstNode = self.adjacency_list[i]

            if firstNode:
                while firstNode:
                    print(firstNode.data, end = " ")
                    firstNode = firstNode.next
                print()

if __name__ == '__main__':
    
    n = int(input("Enter the number of Vertices: "))
    graph = Graph(n)

    print("For adding an edge, press 1")
    print("For removing an edge, press 2")
    print("For displaying the graph, press 3")
    print("For quitting the program, press 4")
    while True:
        choice = int(input("Enter you choice: "))
        
        if choice == 1:
            source, destination = list(map(int, input().split()))
            graph.add_edge(source, destination)

        elif choice == 2:
            source, destination = list(map(int, input().split()))
            graph.remove_edge(source, destination)

        elif choice == 3:
            graph.display_graph()

        elif choice == 4:
            break

        else:
            print("Invalid choice given, try again!")