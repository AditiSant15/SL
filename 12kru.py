class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Already connected

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True

def kruskal_mst(vertices, edges):
    edges.sort()  # Sort by weight
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# Main program
if __name__ == "__main__":
    print("Enter number of vertices:")
    V = int(input())

    print("Enter number of edges:")
    E = int(input())

    edges = []
    print("Enter each edge in the format: u v weight (0-indexed vertices)")
    for _ in range(E):
        u, v, w = map(int, input("Edge (u v weight): ").split())
        edges.append((w, u, v))

    mst, cost = kruskal_mst(V, edges)

    print("\nEdges in Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")
    print("Total cost of MST:", cost)

"""Enter number of vertices:
4
Enter number of edges:
5
Enter each edge in the format: u v weight (0-indexed vertices)
Edge (u v weight): 0 1 10
Edge (u v weight): 0 2 6
Edge (u v weight): 0 3 5
Edge (u v weight): 1 3 15
Edge (u v weight): 2 3 4

Edges in Minimum Spanning Tree:
2 - 3 : 4
0 - 3 : 5
0 - 1 : 10
Total cost of MST: 19
"""