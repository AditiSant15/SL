from queue import PriorityQueue

# Input the number of edges
n = int(input("Number of edges: "))
graph = {}
nodes = set()

# Build the undirected weighted graph
for _ in range(n):
    u, v, cost = input("Edge (u v cost): ").split()
    cost = float(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))
    nodes.update([u, v])

# Input heuristic values
h = {}
m = int(input("Number of heuristic values: "))
print("Enter heuristic (node value):")
for _ in range(m):
    node, val = input().split()
    h[node] = float(val)

# Input start and goal nodes
start = input("Start node: ")
goal = input("Goal node: ")


def a_star(graph, start, goal, h):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    visited = set()

    # Initialize g and f scores
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = h.get(start, 0)

    while not open_set.empty():
        _, current = open_set.get()

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h.get(neighbor, 0)
                open_set.put((f_score[neighbor], neighbor))

    return None


# Run A* algorithm
path = a_star(graph, start, goal, h)

# Output result
if path:
    print("Path:", " -> ".join(path))
else:
    print("No path found")

print("\nName: ADITI SANT, Roll No: TEBD23211, Batch: B1")
