from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, source, destination):
        # Undirected graph: store the edge in both lists.
        self.adj[source].append(destination)
        self.adj[destination].append(source)

    def display_graph(self):
        print("\nAdjacency List:")
        for vertex in range(self.vertices):
            print(f"{vertex} -> {self.adj[vertex]}")

    def bfs(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            print("Invalid starting vertex.")
            return []

        visited = [False] * self.vertices
        queue = deque([start_vertex])
        visited[start_vertex] = True
        traversal = []

        while queue:
            vertex = queue.popleft()
            traversal.append(vertex)

            # Visit adjacent vertices in ascending order.
            for neighbour in sorted(self.adj[vertex]):
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

        return traversal


def main():
    vertices = int(input("Enter number of vertices: "))
    if vertices <= 0:
        print("Number of vertices must be greater than zero.")
        return

    graph = Graph(vertices)

    edges = int(input("Enter number of edges: "))
    if edges < 0:
        print("Number of edges cannot be negative.")
        return

    print("Enter each edge as source and destination (0 to",
          vertices - 1, "):")
    for i in range(edges):
        source, destination = map(
            int, input(f"Edge {i + 1}: ").split()
        )

        if (0 <= source < vertices and
                0 <= destination < vertices):
            graph.add_edge(source, destination)
        else:
            print("Invalid edge. Please enter valid vertex numbers.")
            return

    graph.display_graph()

    start = int(input("\nEnter starting vertex for BFS: "))
    traversal = graph.bfs(start)

    if traversal:
        print("BFS Traversal:", " -> ".join(map(str, traversal)))
        if len(traversal) < vertices:
            print("Unreachable vertices:",
                  *[v for v in range(vertices)
                    if v not in traversal])


if __name__ == "__main__":
    main()
