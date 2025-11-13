import sys

def dijkstra(graph, start_vertex):
    V = len(graph)
    visited = [False] * V
    distance = [sys.maxsize] * V
    distance[start_vertex] = 0

    for _ in range(V):
        min_dist = sys.maxsize
        min_index = -1
        for i in range(V):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        if min_index == -1:
            break  # All remaining vertices are unreachable

        u = min_index
        visited[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not visited[v]:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]

    print(f"\nShortest distances from vertex {start_vertex}:")
    for i in range(V):
        print(f"To vertex {i}: {distance[i] if distance[i] != sys.maxsize else '∞'}")


# -------------------------------
#     GREEDY SELECTION SORT
# -------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print("\nSorted array using Greedy Selection Sort:")
    print(arr)


# -------------------------------
#              MENU
# -------------------------------
def menu():
    while True:
        print("\n======= MENU =======")
        print("1. Dijkstra's Shortest Path Algorithm")
        print("2. Greedy Selection Sort")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        # ---- DIJKSTRA ----
        if choice == '1':
            V = int(input("Enter number of vertices: "))
            graph = []
            print("Enter the adjacency matrix (0 for no edge):")
            for i in range(V):
                row = []
                for j in range(V):
                    weight = int(input(f"Weight from {i} to {j}: "))
                    row.append(weight)
                graph.append(row)
            start = int(input("Enter starting vertex: "))
            if start >= V:
                print("Invalid start vertex.")
            else:
                dijkstra(graph, start)

        # ---- GREEDY SELECTION SORT ----
        elif choice == '2':
            n = int(input("Enter number of elements: "))
            arr = []
            print("Enter the elements:")
            for i in range(n):
                arr.append(int(input(f"Element {i+1}: ")))

            selection_sort(arr)

        # ---- EXIT ----
        elif choice == '3':
            print("Exiting program.")
            print("Name: Aditi Sant , Roll no: TEBD23211 , Batch: B1")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the menu
menu()
