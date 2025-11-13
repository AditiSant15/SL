from collections import deque
def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}
num_nodes = int(input("Enter number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

print("\nName- ADITI SANT, Roll No-23211, Batch-B1")
print("\nDFS Traversal:")
visited_dfs = set()
for node in graph:
    if node not in visited_dfs:
        dfs(graph, node, visited_dfs)

print("\nBFS Traversal:")
visited_bfs = set()
for node in graph:
    if node not in visited_bfs:
        bfs(graph, node, visited_bfs)
