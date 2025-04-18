#Find minimum weight cycle in an undirected graph


import heapq

class Solution:
    # Construct adjacency list
    def constructadj(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))
        return adj

    # Dijkstra's to find shortest path avoiding one edge
    def shortestPath(self, V, adj, src, dest):
        dist = [float('inf')] * V
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if (u == src and v == dest) or (u == dest and v == src):
                    continue
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist[dest]

    # Main function to find minimum weight cycle
    def findMinCycle(self, V, edges):
        adj = self.constructadj(V, edges)
        minCycle = float('inf')
        for edge in edges:
            u, v, w = edge
            dist = self.shortestPath(V, adj, u, v)
            if dist != float('inf'):
                minCycle = min(minCycle, dist + w)
        return -1 if minCycle == float('inf') else minCycle


# ------------------ User Input Section ------------------

def run_with_user_input():
    print("Enter number of vertices:")
    V = int(input())
    print("Enter number of edges:")
    E = int(input())
    edges = []

    print(f"Enter {E} edges in format: u v w")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        edges.append([v, u, w])  # since the graph is undirected

    obj = Solution()
    result = obj.findMinCycle(V, edges)
    print("Minimum weight cycle:", result)


# ------------------ Inbuilt Test Case ------------------

def run_with_inbuilt_test():
    V = 4
    edges = [
        [0, 1, 1],
        [1, 2, 1],
        [2, 0, 1],
        [1, 3, 2]
    ]
    # add reverse edges for undirected graph
    edges += [[v, u, w] for u, v, w in edges]

    obj = Solution()
    result = obj.findMinCycle(V, edges)
    print("Inbuilt Test - Minimum weight cycle:", result)


# ------------------ Main Run ------------------

if __name__ == "__main__":
    print("Choose input type:\n1. User Input\n2. Inbuilt Test Case")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        run_with_user_input()
    elif choice == '2':
        run_with_inbuilt_test()
    else:
        print("Invalid choice.")
