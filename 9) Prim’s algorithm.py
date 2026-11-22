#Represent a given graph using an adjacency adjacency matrix and generate a minimum spanning tree using Prim’s algorithm
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [
            [0 for _ in range(vertices)]
            for _ in range(vertices)
        ]

    def add_edge(self, source, destination, weight):
        # Undirected weighted graph.
        self.adj[source][destination] = weight
        self.adj[destination][source] = weight

    def display_graph(self):
        print("\nWeighted Adjacency Matrix:")
        print("   ", *range(self.vertices))
        for i in range(self.vertices):
            print(i, self.adj[i])

    def prim_mst(self, start):
        if start < 0 or start >= self.vertices:
            print("Invalid starting vertex.")
            return

        INF = float("inf")
        key = [INF] * self.vertices
        parent = [-1] * self.vertices
        in_mst = [False] * self.vertices

        key[start] = 0

        for _ in range(self.vertices):
            # Select the unvisited vertex with minimum key.
            min_key = INF
            u = -1

            for v in range(self.vertices):
                if not in_mst[v] and key[v] < min_key:
                    min_key = key[v]
                    u = v

            # No reachable unvisited vertex: graph is disconnected.
            if u == -1:
                print("Graph is disconnected.")
                print("A spanning tree cannot be formed.")
                return

            in_mst[u] = True

            # Update keys of adjacent, unvisited vertices.
            for v in range(self.vertices):
                weight = self.adj[u][v]
                if (weight > 0 and not in_mst[v]
                        and weight < key[v]):
                    key[v] = weight
                    parent[v] = u

        print("\nMinimum Spanning Tree (MST):")
        print("Edge\tWeight")
        total_cost = 0

        for v in range(self.vertices):
            if parent[v] != -1:
                weight = self.adj[v][parent[v]]
                print(f"{parent[v]} - {v}\t{weight}")
                total_cost += weight

        print("Total Minimum Cost:", total_cost)


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

    print("Enter each edge as: source destination weight")
    print(f"Valid vertices: 0 to {vertices - 1}")

    for i in range(edges):
        source, destination, weight = map(
            int, input(f"Edge {i + 1}: ").split()
        )

        if not (0 <= source < vertices and
                0 <= destination < vertices):
            print("Invalid vertex number.")
            return

        if source == destination:
            print("Self-loops are not accepted in this program.")
            return

        if weight <= 0:
            print("Edge weight must be positive.")
            return

        graph.add_edge(source, destination, weight)

    graph.display_graph()

    start = int(input("\nEnter starting vertex for Prim's algorithm: "))
    graph.prim_mst(start)


if __name__ == "__main__":
    main()
