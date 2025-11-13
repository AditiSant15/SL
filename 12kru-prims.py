# Greedy Search Algorithm for Minimum Spanning Tree
# User chooses either Prim's or Kruskal's Algorithm (one-time choice)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # for Kruskal
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]  # for Prim

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.adj[u][v] = w
        self.adj[v][u] = w  # undirected graph

    # ---------- PRIM'S ALGORITHM ----------
    def prim_mst(self):
        print("\nRunning Prim's Algorithm...")
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        mstSet = [False] * self.V
        key[0] = 0

        for _ in range(self.V):
            u = self.min_key(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.adj[u][v] > 0 and not mstSet[v] and key[v] > self.adj[u][v]:
                    key[v] = self.adj[u][v]
                    parent[v] = u

        self.print_prim_mst(parent)

    def min_key(self, key, mstSet):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v
        return min_index

    def print_prim_mst(self, parent):
        print("\nEdge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t {self.adj[i][parent[i]]}")
            total_weight += self.adj[i][parent[i]]
        print("Total Weight of MST:", total_weight)

    # ---------- KRUSKAL'S ALGORITHM ----------
    def kruskal_mst(self):
        print("\nRunning Kruskal's Algorithm...")
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("\nEdge \tWeight")
        total_weight = 0
        for u, v, weight in result:
            print(f"{u} - {v} \t {weight}")
            total_weight += weight
        print("Total Weight of MST:", total_weight)

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


# ---------- MAIN PROGRAM ----------
def main():
    print("=== Greedy Search Algorithm (MST) ===")
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    g = Graph(V)
    print("\nEnter edges in the format: u v w")
    print("(where u and v are vertices, w is weight)")

    for _ in range(E):
        u, v, w = map(int, input("Edge: ").split())
        g.add_edge(u, v, w)

    print("\nChoose the algorithm:")
    print("1. Prim's Algorithm")
    print("2. Kruskal's Algorithm")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        g.prim_mst()
    elif choice == '2':
        g.kruskal_mst()
    else:
        print("Invalid choice! Exiting...")

if __name__ == "__main__":
    main()


"""
=== Greedy Search Algorithm (MST) ===
Enter the number of vertices: 4
Enter the number of edges: 5

Enter edges in the format: u v w
Edge: 0 1 10
Edge: 0 2 6
Edge: 0 3 5
Edge: 1 3 15
Edge: 2 3 4

Choose the algorithm:
1. Prim's Algorithm
2. Kruskal's Algorithm
Enter your choice (1 or 2): 2

Running Kruskal's Algorithm...

Edge    Weight
2 - 3    4
0 - 3    5
0 - 1    10
Total Weight of MST: 19
"""
