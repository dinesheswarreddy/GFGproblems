#Bellman-Ford

class Solution:
    def bellmanFord(self, V, edges, src):
        INF = 100000000
        dist = [INF] * V
        dist[src] = 0

        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]  # Negative cycle detected

        return dist


def run_inbuilt_test():
    print("\nRunning inbuilt test case:")
    V = 5
    edges = [
        [1, 3, 2],
        [4, 3, -1],
        [2, 4, 1],
        [1, 2, 1],
        [0, 1, 5]
    ]
    src = 0
    sol = Solution()
    result = sol.bellmanFord(V, edges, src)
    print("Output:", result)


def run_user_input():
    print("Enter graph input:")
    V = int(input("Enter number of vertices (V): "))
    E = int(input("Enter number of edges (E): "))
    print("Enter edges in the format: u v w")
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    src = int(input("Enter the source vertex (src): "))

    sol = Solution()
    result = sol.bellmanFord(V, edges, src)
    print("Output:", result)


if __name__ == "__main__":
    print("Choose mode:\n1. Inbuilt Test Case\n2. Custom User Input")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        run_inbuilt_test()
    elif choice == "2":
        run_user_input()
    else:
        print("Invalid choice. Please enter 1 or 2.")
