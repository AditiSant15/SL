import heapq

def dijkstra_mst(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, parent_node)
    mst_cost = 0
    mst_edges = []

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        mst_cost += weight
        if parent is not None:
            mst_edges.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return mst_cost, mst_edges

def take_graph_input():
    graph = {}
    n = int(input("Enter number of vertices: "))
    print("Enter the vertices (space separated):")
    vertices = input().split()

    for v in vertices:
        graph[v] = []

    e = int(input("Enter number of edges: "))
    print("Enter each edge in the format: node1 node2 weight")
    for _ in range(e):
        u, v, w = input().split()
        w = int(w)

        # Since MST is on undirected graphs, add edge both ways
        graph[u].append((v, w))
        graph[v].append((u, w))

    start = input("Enter the starting vertex for MST: ")
    return graph, start

# Main program
graph, start = take_graph_input()
cost, mst = dijkstra_mst(graph, start)

print(f"\nTotal cost of MST: {cost}")
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} (weight {w})")


"""Enter number of vertices: 4
Enter the vertices (space separated):
A B C D
Enter number of edges: 5
Enter each edge in the format: node1 node2 weight
A B 1 
A C 4
B C 2
B D 5
C D 1
Enter the starting vertex for MST: A

Total cost of MST: 4
Edges in MST:
A -- B (weight 1)
B -- C (weight 2)
C -- D (weight 1)"""
