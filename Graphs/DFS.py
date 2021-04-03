from UndirectedGraphUsingList import Graph

def DFS(source, graph):
    visited = [0]*graph.numberOfVertices
    res = []

    def DFSUtil(source):
        nonlocal visited, graph, res
        if visited[source] == 0:
            res.append(source)
            visited[source] = 1

            nodes = graph.adjacency_list[source]
            while nodes:
                DFSUtil(nodes.data)
                nodes = nodes.next
    
    DFSUtil(source)

    return res


if __name__ == '__main__':
    # Take input of number of vertices and edges
    n, m = list(map(int, input().split()))
    graph = Graph(n)

    for _ in range(m):
        # Add source and destination for each edge
        s, d = list(map(int, input().split()))
        graph.add_edge(s, d)
    
    print(*DFS(int(input("Enter the starting vertex: ")), graph))