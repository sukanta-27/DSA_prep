from UndirectedGraphUsingList import Graph

def BFS(source, graph):
    visited = [0]*graph.numberOfVertices
    queue = []
    res = []
    
    # Setup the initial phase
    queue.append(source)
    visited[source] = 1

    while len(queue) > 0:
        node = queue.pop(0)
        res.append(node)

        adjacent_nodes = graph.adjacency_list[node]

        while adjacent_nodes:
            if visited[adjacent_nodes.data] == 0:
                queue.append(adjacent_nodes.data)
                visited[adjacent_nodes.data] = 1
            adjacent_nodes = adjacent_nodes.next
            
    return res


if __name__ == '__main__':
    # Take input of number of vertices and edges
    n, m = list(map(int, input().split()))
    graph = Graph(n)

    for _ in range(m):
        # Add source and destination for each edge
        s, d = list(map(int, input().split()))
        graph.add_edge(s, d)
    
    print(*BFS(int(input("Enter the starting vertex: ")), graph))