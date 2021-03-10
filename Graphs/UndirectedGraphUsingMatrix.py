class Graph:

    def __init__(self, numberOfVertices):
        self.adjacency_matrix = []
        self.numberOfVertices = numberOfVertices
        for _ in range(self.numberOfVertices):
            self.adjacency_matrix.append([0 for j in range(self.numberOfVertices)])

    def add_edge(self, source, destination):
        if source < 0 or source >= self.numberOfVertices or destination < 0 or destination >= self.numberOfVertices:
            print("Invalid Source or Destination given")
            return
        
        if self.adjacency_matrix[source][destination] == 1:
            print("Edge is already present between {} and {}".format(source, destination))
            return

        self.adjacency_matrix[source][destination] = 1
        self.adjacency_matrix[destination][source] = 1 

    def remove_edge(self, source, destination):
        if source < 0 or source >= self.numberOfVertices or destination < 0 or destination >= self.numberOfVertices:
            print("Invalid Source or Destination given")
            return
        
        if self.adjacency_matrix[source][destination] == 0:
            print("No edge present between {} and {}".format(source, destination))
            return

        self.adjacency_matrix[source][destination] = 0
        self.adjacency_matrix[destination][source] = 0 

    def display_graph(self):
        for i in self.adjacency_matrix:
            print(*i)


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