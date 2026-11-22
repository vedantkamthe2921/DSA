class graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.g = [[0 for i in range(9)] for j in range(9)]

    def create(self):
        self.v = int(input("Enter no of vertices: "))
        self.e = int(input("Enter no of edges: "))

        for i in range(self.e):
            print(f"Enter edge {i + 1}")
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            w = int(input("Enter weight: "))

            self.g[u][v] = self.g[v][u] = w

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.g[i][j], end=" ")
            print()


class stack:
    def __init__(self):
        self.st = []
        self.TOP = -1

    def push(self, x):
        self.st.append(x)
        self.TOP += 1

    def pop(self):
        x = self.st[self.TOP]
        self.st.pop()
        self.TOP -= 1
        return x


def dfs(ob, start):
    visited = [False] * ob.v

    s = stack()
    s.push(start)

    while s.TOP != -1:
        u = s.pop()

        if visited[u] == False:
            print(u, end=" ")
            visited[u] = True

            for v in range(ob.v - 1, -1, -1):
                if ob.g[u][v] != 0 and visited[v] == False:
                    s.push(v)


ob = graph()

ob.create()
ob.display()

start = int(input("Enter start vertex: "))

dfs(ob, start)
