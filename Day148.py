#Dijkstra Algorithm

import heapq
from collections import defaultdict

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Since the graph is undirected

        # Initialize distances and priority queue
        dist = [float('inf')] * V
        dist[src] = 0
        min_heap = [(0, src)]  # (distance, vertex)

        # Dijkstra's algorithm
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)
            if curr_dist > dist[u]:
                continue
            for v, weight in adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))

        return dist


def main():
    use_user_input = input("Use custom input? (y/n): ").strip().lower()

    if use_user_input == 'y':
        V = int(input("Enter number of vertices (V): "))
        E = int(input("Enter number of edges (E): "))
        edges = []
        print("Enter edges in the format 'u v w' (without quotes):")
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
        src = int(input("Enter the source vertex: "))
    else:
        # Inbuilt example
        V = 5
        edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
        src = 0
        print("Using inbuilt example:")
        print(f"V = {V}")
        print(f"edges = {edges}")
        print(f"src = {src}")

    sol = Solution()
    result = sol.dijkstra(V, edges, src)
    print("Shortest distances from source:", result)


if __name__ == "__main__":
    main()
